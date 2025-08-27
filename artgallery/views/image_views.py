from rest_framework import viewsets, filters, permissions
from artgallery.models import Image
from artgallery.serializers import PublicImageSerializer as ImageSerializer, AdminImageSerializer


class PublishedImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Image.objects.filter(is_published=True).order_by("order", "-created_at")
    serializer_class = ImageSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "description"]
    ordering_fields = ["created_at", "order"]

class AdminImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all().order_by("order", "-created_at")
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAdminUser]  # only superuser/staff via session login
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "description"]
    ordering_fields = ["created_at", "order"]