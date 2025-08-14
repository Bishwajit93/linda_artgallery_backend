# serializers/video_serializer.py
from rest_framework import serializers
from ..models import Video

class VideoSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField(read_only=True)
    poster_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Video
        fields = [
            "id", "title", "description",
            "file", "poster",              # writable (multipart)
            "file_url", "poster_url",      # read-only resolved URLs
            "size_label", "recorded_at", "duration_seconds",
            "order", "is_published", "created_at",
        ]
        read_only_fields = ["created_at", "file_url", "poster_url"]

    def _abs_url(self, url: str | None) -> str | None:
        """Return absolute URL; if already absolute, keep it; otherwise build from request if available."""
        if not url:
            return None
        if url.startswith("http://") or url.startswith("https://"):
            return url
        req = self.context.get("request")
        return req.build_absolute_uri(url) if req else url

    def get_file_url(self, obj):
        return self._abs_url(getattr(obj.file, "url", None))

    def get_poster_url(self, obj):
        return self._abs_url(getattr(obj.poster, "url", None))


# serializers/image_serializer.py
from rest_framework import serializers
from ..models import Image

class ImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Image
        fields = [
            "id", "title", "description",
            "image",        # writable (multipart)
            "image_url",    # read-only resolved URL
            "is_published", "order", "created_at",
        ]
        read_only_fields = ["created_at", "image_url"]

    def _abs_url(self, url: str | None) -> str | None:
        """Return absolute URL; if already absolute, keep it; otherwise build from request if available."""
        if not url:
            return None
        if url.startswith("http://") or url.startswith("https://"):
            return url
        req = self.context.get("request")
        return req.build_absolute_uri(url) if req else url

    def get_image_url(self, obj):
        return self._abs_url(getattr(obj.image, "url", None))
