from rest_framework import serializers
from artgallery.models import Video
import os

CLOUD_NAME = os.getenv("CLOUDINARY_CLOUD_NAME", "").strip()

def _abs(url: str) -> str:
    if not url:
        return url
    if url.startswith("http://") or url.startswith("https://"):
        return url
    base = f"https://res.cloudinary.com/{CLOUD_NAME}/" if CLOUD_NAME else ""
    return base + url.lstrip("/")

class PublicVideoSerializer(serializers.ModelSerializer):
    # Return absolute URL for the video file
    video = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S")

    class Meta:
        model = Video
        fields = (
            "id",
            "title",
            "description",
            "video",
            "is_published",
            "order",
            "created_at",
        )

    def get_video(self, obj):
        path = str(obj.video) if obj.video else ""
        return _abs(path)

class AdminVideoSerializer(PublicVideoSerializer):
    class Meta(PublicVideoSerializer.Meta):
        pass
