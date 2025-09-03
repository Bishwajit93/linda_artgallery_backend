from rest_framework import viewsets
from artgallery.models.artwork import Artwork, ArtworkImage, ArtworkVideo
from artgallery.serializers.artwork_serializers import (
    ArtworkSerializer,
    ArtworkImageSerializer,
    ArtworkVideoSerializer,
)


# --------------------------------------------------
# Artwork ViewSet
# --------------------------------------------------
class ArtworkViewSet(viewsets.ModelViewSet):
    serializer_class = ArtworkSerializer

    def get_queryset(self):
        """
        If the user is staff (admin panel), return all artworks.
        Otherwise, only return published artworks.
        """
        qs = Artwork.objects.all().order_by("-created_at")
        if not self.request.user.is_staff:
            qs = qs.filter(is_published=True)
        return qs


# --------------------------------------------------
# ArtworkImage ViewSet
# --------------------------------------------------
class ArtworkImageViewSet(viewsets.ModelViewSet):
    serializer_class = ArtworkImageSerializer

    def get_queryset(self):
        """
        If staff → return all images.
        Otherwise → only return images that belong to published artworks.
        """
        qs = ArtworkImage.objects.all().order_by("order", "-uploaded_at")
        if not self.request.user.is_staff:
            qs = qs.filter(artwork__is_published=True)
        return qs


# --------------------------------------------------
# ArtworkVideo ViewSet
# --------------------------------------------------
class ArtworkVideoViewSet(viewsets.ModelViewSet):
    serializer_class = ArtworkVideoSerializer

    def get_queryset(self):
        """
        If staff → return all videos.
        Otherwise → only return videos that belong to published artworks.
        """
        qs = ArtworkVideo.objects.all().order_by("-uploaded_at")
        if not self.request.user.is_staff:
            qs = qs.filter(artwork__is_published=True)
        return qs
