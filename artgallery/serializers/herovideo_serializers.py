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
            "video_url",
        ]

    def get_video_url(self, obj):
        if obj.video:
            return obj.video.url  # ✅ BunnyStorage.url() will return CDN link
        return None
