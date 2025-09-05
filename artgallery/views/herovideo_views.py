from rest_framework import viewsets, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from artgallery.models.herovideo import HeroVideo
from artgallery.serializers.herovideo_serializers import HeroVideoSerializer

class HeroVideoViewSet(viewsets.ModelViewSet):
    serializer_class = HeroVideoSerializer
    queryset = HeroVideo.objects.all().order_by("order", "-created_at")
    parser_classes = [MultiPartParser, FormParser]  # ✅ handle file uploads

    def create(self, request, *args, **kwargs):
        # Ensure file is passed
        if "video" not in request.FILES:
            return Response({"error": "No video file provided"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
