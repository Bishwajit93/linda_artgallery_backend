from rest_framework import viewsets, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from artgallery.models.heroimage import HeroImage
from artgallery.serializers.heroimage_serializers import HeroImageSerializer

class HeroImageViewSet(viewsets.ModelViewSet):
    serializer_class = HeroImageSerializer
    queryset = HeroImage.objects.all().order_by("order", "-created_at")
    parser_classes = [MultiPartParser, FormParser]

    def create(self, request, *args, **kwargs):
        print("FILES DEBUG:", request.FILES)  # 👀 Check what’s inside
        if "image" not in request.FILES:
            return Response({"error": "No image file provided"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


