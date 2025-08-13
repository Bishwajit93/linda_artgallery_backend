from rest_framework import serializers
from .models import Video

class VideoSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()
    poster_url = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = [
            "id",
            "title",
            "description",
            "file_url",
            "poster_url",
            "size_label",
            "recorded_at",
            "duration_seconds",
            "order",
            "is_published",
            "created_at",
        ]

    def get_file_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.file.url) if obj.file else None

    def get_poster_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.poster.url) if obj.poster else None
