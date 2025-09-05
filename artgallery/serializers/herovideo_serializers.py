from rest_framework import serializers
from ..models.herovideo import HeroVideo


class HeroVideoSerializer(serializers.ModelSerializer):
    video_url = serializers.SerializerMethodField()

    class Meta:
        model = HeroVideo
        fields = [
            "id",
            "title",
            "description",
            "order",
            "is_active",
            "created_at",
            "video",       # ✅ raw file field (needed for upload)
            "video_url",   # ✅ Bunny CDN URL
        ]

    def get_video_url(self, obj):
        if obj.video and hasattr(obj.video, "url"):
            return obj.video.url
        return None
