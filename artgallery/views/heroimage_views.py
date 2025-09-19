from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from artgallery.models.heroimage import HeroImage
from artgallery.serializers.heroimage_serializers import HeroImageSerializer

class HeroImageViewSet(viewsets.ModelViewSet):
    serializer_class = HeroImageSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        qs = HeroImage.objects.all().order_by("order", "-created_at")
        if not self.request.user.is_staff:
            qs = qs.filter(is_active=True)
        return qs
