## views/video_views.py

from rest_framework import generics
from ..serializers import VideoSerializer
from ..models import Video



class VideoListView(generics.ListAPIView):
    """
    Public endpoint for the hero/gallery to read videos.
    Sorted by 'order' (ascending) then '-created_at'.
    Only published videos are returned.
    """
    queryset = Video.objects.filter(is_published=True).order_by("order", "-created_at")
    serializer_class = VideoSerializer
    

class VideoDetailView(generics.RetrieveAPIView):
    queryset = Video.objects.filter(is_published=True)
    serializer_class = VideoSerializer
    lookup_field = "id"
