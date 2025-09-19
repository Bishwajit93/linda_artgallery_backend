from rest_framework import serializers
from django.conf import settings
from ..models.heroimage import HeroImage

class HeroImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = HeroImage
        fields = ["id", "title", "image_url", "is_active", "order", "created_at"]

    def get_image_url(self, obj):
        pull_zone = getattr(settings, "BUNNY_PULL_ZONE_URL", None)
        cdn_url = getattr(settings, "BUNNY_CDN_URL", "")
        if obj.image and hasattr(obj.image, "url"):
            storage_url = obj.image.url
            if pull_zone:
                return storage_url.replace(cdn_url.rstrip("/"), pull_zone.rstrip("/"))
            return storage_url
        return None
