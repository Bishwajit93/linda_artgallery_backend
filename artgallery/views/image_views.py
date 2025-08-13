## views/image_views.py

from rest_framework import generics, permissions, parsers, views, response, status
from ..models import Image
from ..serializers import ImageSerializer

class ImageListView(generics.ListAPIView):
    queryset = Image.objects.filter(is_published=True).order_by("order", "-created_at")
    serializer_class = ImageSerializer

class ImageDetailView(generics.RetrieveAPIView):
    queryset = Image.objects.filter(is_published=True)
    serializer_class = ImageSerializer
    lookup_field = "id"

class ImageCreateView(generics.CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    permission_classes = [permissions.AllowAny]

class ImageUpdateView(generics.UpdateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    permission_classes = [permissions.AllowAny]
    lookup_field = "id"

class ImageDeleteView(generics.DestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "id"

class ImageReorderView(views.APIView):
    """
    PATCH /api/images/reorder/
    body: { "orders": [ {"id": 3, "order": 1}, {"id": 8, "order": 2} ] }
    """
    permission_classes = [permissions.AllowAny]

    def patch(self, request):
        items = request.data.get("orders", [])
        if not isinstance(items, list):
            return response.Response({"detail": "orders must be a list"}, status=400)

        to_update = []
        for item in items:
            img_id = item.get("id")
            order  = item.get("order")
            if img_id is None or order is None:
                continue
            try:
                im = Image.objects.get(id=img_id)
                im.order = int(order)
                to_update.append(im)
            except Image.DoesNotExist:
                continue
        if to_update:
            Image.objects.bulk_update(to_update, ["order"])
        return response.Response({"updated": len(to_update)}, status=status.HTTP_200_OK)

class ImagePublishToggleView(views.APIView):
    """
    PATCH /api/images/<id>/publish/
    body: { "is_published": true/false }
    """
    permission_classes = [permissions.AllowAny]

    def patch(self, request, id):
        try:
            im = Image.objects.get(id=id)
        except Image.DoesNotExist:
            return response.Response({"detail": "Not found"}, status=404)
        is_pub = request.data.get("is_published")
        if isinstance(is_pub, bool):
            im.is_published = is_pub
            im.save(update_fields=["is_published"])
            return response.Response({"id": im.id, "is_published": im.is_published})
        return response.Response({"detail": "is_published must be boolean"}, status=400)
