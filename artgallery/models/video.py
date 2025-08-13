## models/video.py

from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to="videos/")  # uploaded video file
    poster = models.ImageField(upload_to="video_posters/", blank=True, null=True)  # optional cover image
    size_label = models.CharField(max_length=32, blank=True)  # e.g. "1920×1080"
    recorded_at = models.DateField(blank=True, null=True)
    duration_seconds = models.PositiveIntegerField(blank=True, null=True)
    order = models.PositiveSmallIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order", "-created_at"]

    def __str__(self):
        return self.title
