from django.urls import path
from .views.video_views import VideoListView, VideoDetailView

urlpatterns = [
    path("videos/", VideoListView.as_view(), name="video-list"),
    path("videos/<int:id>/", VideoDetailView.as_View(), name="veideo-detail"),
]