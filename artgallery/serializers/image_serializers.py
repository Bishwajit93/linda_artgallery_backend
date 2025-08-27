from rest_framework import serializers
from artgallery.models import Image
import os

CLOUD_NAME = os.getenv("CLOUDINARY_CLOUD_NAME", "").strip()

def _abs(url: str) -> str:
    if not url:
        return url
    if url.startswith("http://") or url.startswith("https://"):
        return url
    # Fallback-safe even if CLOUD_NAME missing (will still return relative)
    base = f"https://res.cloudinary.com/{CLOUD_NAME}/" if CLOUD_NAME else ""
    return base + url.lstrip("/")

class PublicImageSerializer(serializers.ModelSerializer):
    # Override the field to return an absolute URL
    image = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S")

    class Meta:
        model = Image
        fields = (
            "id",
            "title",
            "description",
            "height",
            "width",
            "depth",
            "image",
            "is_published",
            "order",
            "created_at",
        )

    def get_image(self, obj):
        path = str(obj.image) if obj.image else ""
        return _abs(path)

class AdminImageSerializer(PublicImageSerializer):
    """
    Same output shape for admin API for consistency.
    If you ever want extra admin-only fields, add here.
    """
    class Meta(PublicImageSerializer.Meta):
        pass


