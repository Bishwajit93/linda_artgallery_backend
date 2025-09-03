# artgallery/models/herovideo.py

from django.db import models
import os


def hero_video_upload_to(instance, filename):
    """
    Custom file naming function for BunnyCDN storage.
    Keeps the original filename but stores it inside 'herovideos/' folder.
    """
    return os.path.join("herovideos", filename)


class HeroVideo(models.Model):
    # Optional title for the video
    title = models.CharField(max_length=255, blank=True, null=True)

    # Optional description for the video
    description = models.TextField(blank=True, null=True)

    # Video file stored on BunnyCDN, inside folder "herovideos"
    video = models.FileField(upload_to=hero_video_upload_to)

    # Display order (lower numbers appear first in the playlist)
    order = models.PositiveSmallIntegerField(default=0)

    # Visibility flag (Linda can hide a video without deleting it)
    is_active = models.BooleanField(default=True)

    # Auto timestamp when created (was in your original model)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order", "-created_at"]

    def __str__(self):
        return self.title if self.title else f"Hero Video {self.id}"
