from rest_framework import serializers
from django.conf import settings
from ..models.herovideo import HeroVideo


class HeroVideoSerializer(serializers.ModelSerializer):
    video_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = HeroVideo
        fields = [
            "id",
            "title",
            "description",
            "order",
            "is_active",
            "created_at",
            "video",       # keep video field so uploads work
            "video_url",   # BunnyCDN-transformed URL
        ]
        extra_kwargs = {
            "video": {"required": False},   # ✅ don't force re-upload on update
        }

    def get_video_url(self, obj):
        if obj.video and hasattr(obj.video, "url"):
            storage_url = obj.video.url
            pull_zone = getattr(settings, "BUNNY_PULL_ZONE_URL", None)
            cdn_url = getattr(settings, "BUNNY_CDN_URL", "")

            if pull_zone and cdn_url:
                return storage_url.replace(cdn_url.rstrip("/"), pull_zone.rstrip("/"))

            return storage_url
        return None
