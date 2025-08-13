# serializers/image_serializer.py

from rest_framework import serializers
from ..models import Image  # your Image model

class ImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Image
        fields = [
            "id", "title", "description",
            "image",            # <— writable file field
            "image_url",        # <— read-only absolute URL
            "is_published", "order", "created_at",
        ]
        read_only_fields = ["created_at", "image_url"]

    def get_image_url(self, obj):
        req = self.context.get("request")
        return req.build_absolute_uri(obj.image.url) if obj.image else None

