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
        # CloudinaryField.url is already an absolute https URL; _abs_url keeps it as-is
        return self._abs_url(getattr(obj.image, "url", None))
