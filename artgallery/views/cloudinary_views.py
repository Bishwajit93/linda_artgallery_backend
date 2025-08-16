import time
import hashlib
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def cloudinary_signature(request):
    """
    Generates a signed upload payload for Cloudinary.
    Frontend calls this before uploading a video.
    """
    timestamp = int(time.time())
    folder = request.GET.get("folder", "linda/videos")

    cloud_name = os.environ.get("CLOUD_NAME")
    api_key = os.environ.get("CLOUD_API_KEY")
    api_secret = os.environ.get("CLOUD_API_SECRET")

    params_to_sign = {
        "timestamp": timestamp,
        "folder": folder,
    }

    # Create signature
    signature_str = "&".join([f"{k}={v}" for k, v in sorted(params_to_sign.items())])
    signature = hashlib.sha1(f"{signature_str}{api_secret}".encode("utf-8")).hexdigest()

    return JsonResponse({
        "signature": signature,
        "timestamp": timestamp,
        "folder": folder,
        "api_key": api_key,
        "cloud_name": cloud_name,
    })
