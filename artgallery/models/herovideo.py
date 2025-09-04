from django.db import models
import os

def hero_video_upload_to(instance, filename):
    return os.path.join("herovideos", filename)

class HeroVideo(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    video = models.FileField(
        upload_to=hero_video_upload_to,
        storage="artgallery.storage_backends.BunnyStorage",  # ✅ use string path
    )

    order = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order", "-created_at"]

    def __str__(self):
        return self.title if self.title else f"Hero Video {self.id}"
