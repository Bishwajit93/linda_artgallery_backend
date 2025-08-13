## views/image_views.py

from rest_framework import generics
from ..models import Image
from ..serializers import ImageSerializer

class ImageListView(generics.ListAPIView):
    queryset = Image.objects.filter(is_published=True).order_by("order", "-created_at")
    serializer_class = ImageSerializer


class ImageDetailView(generics.RetrieveAPIView):
    queryset = Image.objects.filter(is_published=True)
    serializer_class = ImageSerializer
    lookup_field = "id"
