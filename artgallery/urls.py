from django.urls import path
from .views.video_views import VideoListView

urlpatterns = [
    path("videos/", VideoListView.as_view(), name="video-list")
]