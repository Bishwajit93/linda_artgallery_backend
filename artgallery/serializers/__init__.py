from .image_serializers import PublicImageSerializer, AdminImageSerializer
from .video_serializers import PublicVideoSerializer, AdminVideoSerializer

# Backwards-compatible aliases so existing imports keep working
ImageSerializer = PublicImageSerializer
VideoSerializer = PublicVideoSerializer

__all__ = [
    "PublicImageSerializer", "AdminImageSerializer",
    "PublicVideoSerializer", "AdminVideoSerializer",
    "ImageSerializer", "VideoSerializer",
]

