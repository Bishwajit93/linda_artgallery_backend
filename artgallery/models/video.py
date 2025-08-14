from django.db import models
from cloudinary.models import CloudinaryField

class Video(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)

    # ✅ Force Cloudinary to treat this as a video
    file = CloudinaryField(
        "video",
        folder="videos/artworks",
        resource_type="video"
    )

    # ✅ Poster is still an image
    poster = CloudinaryField(
        "image",
        folder="videos/posters",
        blank=True,
        null=True
    )

    size_label = models.CharField(max_length=32, blank=True)
    recorded_at = models.DateField(blank=True, null=True)
    duration_seconds = models.PositiveIntegerField(blank=True, null=True)
    order = models.PositiveSmallIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order", "-created_at"]

    def __str__(self):
        return self.title
