## views/video_views.py

from rest_framework import generics, permissions, parsers, views, response, status
from ..serializers import VideoSerializer
from ..models import Video

class VideoListView(generics.ListAPIView):
    queryset = Video.objects.filter(is_published=True).order_by("order", "-created_at")
    serializer_class = VideoSerializer

class VideoDetailView(generics.RetrieveAPIView):
    queryset = Video.objects.filter(is_published=True)
    serializer_class = VideoSerializer
    lookup_field = "id"

class VideoCreateView(generics.CreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    permission_classes = [permissions.AllowAny]

class VideoUpdateView(generics.UpdateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    permission_classes = [permissions.AllowAny]
    lookup_field = "id"

class VideoDeleteView(generics.DestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "id"

class VideoReorderView(views.APIView):
    """
    PATCH /api/videos/reorder/
    body: { "orders": [ {"id": 12, "order": 1}, {"id": 7, "order": 2}, ... ] }
    """
    permission_classes = [permissions.AllowAny]

    def patch(self, request):
        items = request.data.get("orders", [])
        if not isinstance(items, list):
            return response.Response({"detail": "orders must be a list"}, status=400)

        # bulk update
        to_update = []
        for item in items:
            vid_id = item.get("id")
            order  = item.get("order")
            if vid_id is None or order is None:
                continue
            try:
                v = Video.objects.get(id=vid_id)
                v.order = int(order)
                to_update.append(v)
            except Video.DoesNotExist:
                continue
        if to_update:
            Video.objects.bulk_update(to_update, ["order"])
        return response.Response({"updated": len(to_update)}, status=status.HTTP_200_OK)

class VideoPublishToggleView(views.APIView):
    """
    PATCH /api/videos/<id>/publish/
    body: { "is_published": true/false }
    """
    permission_classes = [permissions.AllowAny]

    def patch(self, request, id):
        try:
            v = Video.objects.get(id=id)
        except Video.DoesNotExist:
            return response.Response({"detail": "Not found"}, status=404)
        is_pub = request.data.get("is_published")
        if isinstance(is_pub, bool):
            v.is_published = is_pub
            v.save(update_fields=["is_published"])
            return response.Response({"id": v.id, "is_published": v.is_published})
        return response.Response({"detail": "is_published must be boolean"}, status=400)
