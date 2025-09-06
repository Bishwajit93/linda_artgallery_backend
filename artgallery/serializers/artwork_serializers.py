from rest_framework import serializers
from django.conf import settings
from ..models.artwork import Artwork, ArtworkImage, ArtworkVideo


# --------------------------------------------------
# ArtworkImage Serializer
# --------------------------------------------------
class ArtworkImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = ArtworkImage
        fields = ["id", "image_url", "height_cm", "width_cm", "order", "uploaded_at"]

    def get_image_url(self, obj):
        pull_zone = getattr(settings, "BUNNY_PULL_ZONE_URL", None)
        cdn_url = getattr(settings, "BUNNY_CDN_URL", "")

        if obj.image and hasattr(obj.image, "url"):
            storage_url = obj.image.url
            if pull_zone:
                return storage_url.replace(cdn_url.rstrip("/"), pull_zone.rstrip("/"))
            return storage_url
        return None



# --------------------------------------------------
# ArtworkVideo Serializer
# --------------------------------------------------
class ArtworkVideoSerializer(serializers.ModelSerializer):
    video_url = serializers.SerializerMethodField()

    class Meta:
        model = ArtworkVideo
        fields = ["id", "video_url", "uploaded_at"]  # ✅ only Pull Zone URL

    def get_video_url(self, obj):
        pull_zone = getattr(settings, "BUNNY_PULL_ZONE_URL", None)
        cdn_url = getattr(settings, "BUNNY_CDN_URL", "")

        if obj.video and hasattr(obj.video, "url"):
            storage_url = obj.video.url
            if pull_zone:
                return storage_url.replace(cdn_url.rstrip("/"), pull_zone.rstrip("/"))
            return storage_url
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
