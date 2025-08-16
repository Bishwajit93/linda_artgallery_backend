from rest_framework import serializers
from ..models import Video

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = [
            "id", "title", "description",
            "file_url", "poster_url",
            "size_label", "recorded_at", "duration_seconds",
            "order", "is_published", "created_at",
        ]
        read_only_fields = ["created_at"]
