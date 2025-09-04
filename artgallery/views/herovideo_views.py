from rest_framework import viewsets, status
from rest_framework.response import Response
from artgallery.models.herovideo import HeroVideo
from artgallery.serializers.herovideo_serializers import HeroVideoSerializer


# --------------------------------------------------
# HeroVideo ViewSet
# --------------------------------------------------
class HeroVideoViewSet(viewsets.ModelViewSet):
    serializer_class = HeroVideoSerializer

    def get_queryset(self):
        """
        If staff → return all hero videos.
        Otherwise → return only active ones.
        """
        qs = HeroVideo.objects.all().order_by("order", "-created_at")
        if not self.request.user.is_staff:
            qs = qs.filter(is_active=True)
        return qs

    def create(self, request, *args, **kwargs):
        """
        Before saving:
        - Check if there are already 5 active videos.
        - If yes → block creation.
        """
        # active_count = HeroVideo.objects.filter(is_active=True).count()
        # if active_count >= 5:
        #     return Response(
        #         {"error": "Maximum of 5 active hero videos allowed."},
        #         status=status.HTTP_400_BAD_REQUEST,
        #     )
        return super().create(request, *args, **kwargs)
