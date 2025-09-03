from rest_framework import serializers
from ..models.artwork import Artwork, ArtworkImage, ArtworkVideo
from django.conf import settings


# --------------------------------------------------
# ArtworkImage Serializer
# --------------------------------------------------
class ArtworkImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = ArtworkImage
        fields = ["id", "image_url", "height_cm", "width_cm", "order", "uploaded_at"]

    def get_image_url(self, obj):
        if obj.image:
            # Always use Bunny CDN URL
            return f"{settings.MEDIA_URL}{obj.image.name}"
        return None


# --------------------------------------------------
# ArtworkVideo Serializer
# --------------------------------------------------
class ArtworkVideoSerializer(serializers.ModelSerializer):
    video_url = serializers.SerializerMethodField()

    class Meta:
        model = ArtworkVideo
        fields = ["id", "video_url", "uploaded_at"]

    def get_video_url(self, obj):
        if obj.video:
            # Always use Bunny CDN URL
            return f"{settings.MEDIA_URL}{obj.video.name}"
        return None


# --------------------------------------------------
# Artwork Serializer
# --------------------------------------------------
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
