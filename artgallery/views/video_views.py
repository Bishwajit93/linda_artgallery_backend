from rest_framework import viewsets, filters, permissions
from artgallery.models import Video
from artgallery.serializers import VideoSerializer

# Public read-only videos
class PublishedVideoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Video.objects.filter(is_published=True).order_by("order", "-created_at")
    serializer_class = VideoSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "description"]
    ordering_fields = ["created_at", "order"]

# Admin-only full CRUD
class AdminVideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all().order_by("order", "-created_at")
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAdminUser]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "description"]
    ordering_fields = ["created_at", "order"]
