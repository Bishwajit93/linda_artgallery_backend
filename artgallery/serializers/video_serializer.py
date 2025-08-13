## serializers/video_serializer.py

from rest_framework import serializers
from ..models import Video

class VideoSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField(read_only=True)
    poster_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Video
        # include real fields for write, computed URLs for read
        fields = [
            "id", "title", "description",
            "file", "poster",              # <— writable file fields
            "file_url", "poster_url",      # <— read-only
            "size_label", "recorded_at", "duration_seconds",
            "order", "is_published", "created_at",
        ]
        read_only_fields = ["created_at", "file_url", "poster_url"]

    def get_file_url(self, obj):
        req = self.context.get("request")
        if obj.file and req:
            url = req.build_absolute_uri(obj.file.url)
            # Force HTTPS for production
            if url.startswith("http://"):
                url = url.replace("http://", "https://")
            return url
        return None

    def get_poster_url(self, obj):
        req = self.context.get("request")
        if obj.poster and req:
            url = req.build_absolute_uri(obj.poster.url)
            if url.startswith("http://"):
                url = url.replace("http://", "https://")
            return url
        return None

