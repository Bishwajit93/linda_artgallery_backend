from rest_framework import viewsets, status
from rest_framework.response import Response

from artgallery.models.herovideo import HeroVideo
from artgallery.serializers.herovideo_serializers import HeroVideoSerializer


# --------------------------------------------------
# HeroVideo ViewSet
# --------------------------------------------------
class HeroVideoViewSet(viewsets.ModelViewSet):
    """
    API endpoints for Hero Videos.
    - List: GET /api/hero-videos/
    - Retrieve: GET /api/hero-videos/{id}/
    - Create: POST /api/hero-videos/
    - Update: PUT/PATCH /api/hero-videos/{id}/
    - Delete: DELETE /api/hero-videos/{id}/
    """
    serializer_class = HeroVideoSerializer

    def get_queryset(self):
        """
        Staff users → return all videos.
        Normal users → return only active ones.
        """
        qs = HeroVideo.objects.all().order_by("order", "-created_at")
        if not self.request.user.is_staff:
            qs = qs.filter(is_active=True)
        return qs

    def create(self, request, *args, **kwargs):
        """
        Create a new HeroVideo.
        (✅ Removed the "max 5" restriction for now.)
        """
        return super().create(request, *args, **kwargs)
