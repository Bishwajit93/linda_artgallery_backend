from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    # Cloudinary URLs (store only URLs)
    file_url = models.URLField(max_length=500, blank=True, null=True)
    poster_url = models.URLField(max_length=500, blank=True, null=True)

    size_label = models.CharField(max_length=50, blank=True, null=True)
    recorded_at = models.DateTimeField(blank=True, null=True)
    duration_seconds = models.IntegerField(blank=True, null=True)

    order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Video {self.id}"
