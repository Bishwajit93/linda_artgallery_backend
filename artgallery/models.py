from django.db import models

class HeroSection(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    background_image = models.ImageField(upload_to='hero_images/', blank=True, null=True)
    background_video = models.FileField(upload_to='hero_videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or "Untitled Hero Section"
