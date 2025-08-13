# serializers/image_serializer.py

from rest_framework import serializers
from ..models import Image

class ImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = [
            "id",
            "title",
            "description",
            "image_url",
            "is_published",
            "order",
            "created_at",
        ]

    def get_image_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image.url) if obj.image else None
