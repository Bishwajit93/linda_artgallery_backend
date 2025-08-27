from django.db import models
from cloudinary.models import CloudinaryField
from django.core.validators import FileExtensionValidator

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    video = CloudinaryField(
        "video",
        resource_type="video",
        folder="linda_artgallery/videos/artworks",
        validators=[FileExtensionValidator(allowed_extensions=["mp4","mov","webm","mkv","m4v","avi"])],
    )


    is_published = models.BooleanField(default=False)
    order = models.PositiveSmallIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    
    # ... existing imports and Video model ...

    class Meta:
        ordering = ["order", "-created_at"]
        db_table = "gallery_video"

    def __str__(self):
        return self.title or f"Video #{self.pk}"
