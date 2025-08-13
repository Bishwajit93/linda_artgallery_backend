from django.urls import path
from .views.video_views import VideoListView, VideoDetailView
from .views.image_views import ImageListView, ImageDetailView

urlpatterns = [
    path("videos/", VideoListView.as_view(), name="video-list"),
    path("videos/<int:id>/", VideoDetailView.as_view(), name="video-detail"),
    path("images/", ImageListView.as_view(), name="image-list"),
    path("images/<int:id>/", ImageDetailView.as_view(), name="image-detail"),
]
