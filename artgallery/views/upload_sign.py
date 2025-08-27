# artgallery/views/upload_sign.py
import os, time, hashlib, re
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, status
from rest_framework.response import Response

API_KEY = os.getenv("CLOUDINARY_API_KEY")
API_SECRET = os.getenv("CLOUDINARY_API_SECRET")
CLOUD_NAME = os.getenv("CLOUDINARY_CLOUD_NAME")
BASE_FOLDER = os.getenv("CLOUDINARY_BASE_FOLDER", "linda_artgallery")

ALLOWED_IMAGE_EXTS = ["jpg", "jpeg", "png", "webp", "heic"]
ALLOWED_VIDEO_EXTS = ["mp4", "mov", "webm", "mkv", "m4v", "avi"]

def _sign(params: dict) -> str:
    # Cloudinary signing: sort keys, join as key=value with & (exclude None/empty), then sha1 with API_SECRET suffix
    to_sign = "&".join(f"{k}={v}" for k, v in sorted(params.items()) if v not in [None, ""])
    return hashlib.sha1(f"{to_sign}{API_SECRET}".encode("utf-8")).hexdigest()

def _sanitize_subfolder(s: str) -> str:
    s = (s or "").strip().lstrip("/")  # trim & remove leading slash
    s = re.sub(r"\.\.", "", s)         # block parent-dir refs
    return s

@api_view(["POST"])
@permission_classes([permissions.IsAdminUser])  # only staff/admin
def sign_upload(request):
    """
    Create a signature for a direct browser upload.
    Frontend sends: { resource_type: "video" | "image", subfolder?: "videos/artworks" | "images/artworks", public_id?: "..." }
    """
    if not (API_KEY and API_SECRET and CLOUD_NAME):
        return Response({"detail": "Cloudinary credentials not set"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    resource_type = (request.data.get("resource_type") or "image").strip().lower()
    if resource_type not in ("image", "video"):
        resource_type = "image"

    subfolder = _sanitize_subfolder(request.data.get("subfolder", ""))  # e.g. "videos/artworks"
    public_id = request.data.get("public_id") or None

    # Force assets to stay inside our project base folder
    folder = f"{BASE_FOLDER}/{subfolder}".strip("/")

    # Allowed formats (extra server-side gate)
    allowed_formats = ",".join(ALLOWED_VIDEO_EXTS if resource_type == "video" else ALLOWED_IMAGE_EXTS)

    ts = int(time.time())
    params_to_sign = {
        "timestamp": ts,
        "folder": folder,
        "use_filename": "true",
        "unique_filename": "true",
        "allowed_formats": allowed_formats,
    }
    if public_id:
        params_to_sign["public_id"] = public_id

    signature = _sign(params_to_sign)
    return Response({
        "cloud_name": CLOUD_NAME,
        "api_key": API_KEY,
        "timestamp": ts,
        "signature": signature,
        "folder": folder,
        "resource_type": resource_type,   # the frontend must call the matching /image/upload or /video/upload
        "allowed_formats": allowed_formats,
    })
