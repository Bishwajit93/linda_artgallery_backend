from rest_framework import serializers
from ..models.artwork import Artwork, ArtworkImage, ArtworkVideo


class ArtworkImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = ArtworkImage
        fields = ["id", "image", "image_url", "height_cm", "width_cm", "order", "uploaded_at"]

    def get_image_url(self, obj):
        if obj.image and hasattr(obj.image, "url"):
            return obj.image.url
        return None


class ArtworkVideoSerializer(serializers.ModelSerializer):
    video_url = serializers.SerializerMethodField()

    class Meta:
        model = ArtworkVideo
        fields = ["id", "video", "video_url", "uploaded_at"]

    def get_video_url(self, obj):
        if obj.video and hasattr(obj.video, "url"):
            return obj.video.url
        return None


class ArtworkSerializer(serializers.ModelSerializer):
    images = ArtworkImageSerializer(many=True, read_only=True)
    videos = ArtworkVideoSerializer(many=True, read_only=True)

    class Meta:
        model = Artwork
        fields = [
            "id",
            "title",
            "description",
            "category",
            "is_published",
            "created_at",
            "images",
            "videos",
        ]
