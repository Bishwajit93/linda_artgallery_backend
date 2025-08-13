from django.urls import path
from .views import video_views, image_views

urlpatterns = [
    # Videos
    path("videos/", video_views.VideoListView.as_view(), name="video-list"),
    path("videos/<int:id>/", video_views.VideoDetailView.as_view(), name="video-detail"),
    path("videos/upload/", video_views.VideoCreateView.as_view(), name="video-upload"),
    path("videos/<int:id>/update/", video_views.VideoUpdateView.as_view(), name="video-update"),
    path("videos/<int:id>/delete/", video_views.VideoDeleteView.as_view(), name="video-delete"),
    path("videos/reorder/", video_views.VideoReorderView.as_view(), name="video-reorder"),
    path("videos/<int:id>/publish/", video_views.VideoPublishToggleView.as_view(), name="video-publish"),

    # Images
    path("images/", image_views.ImageListView.as_view(), name="image-list"),
    path("images/<int:id>/", image_views.ImageDetailView.as_view(), name="image-detail"),
    path("images/upload/", image_views.ImageCreateView.as_view(), name="image-upload"),
    path("images/<int:id>/update/", image_views.ImageUpdateView.as_view(), name="image-update"),
    path("images/<int:id>/delete/", image_views.ImageDeleteView.as_view(), name="image-delete"),
    path("images/reorder/", image_views.ImageReorderView.as_view(), name="image-reorder"),
    path("images/<int:id>/publish/", image_views.ImagePublishToggleView.as_view(), name="image-publish"),
]
