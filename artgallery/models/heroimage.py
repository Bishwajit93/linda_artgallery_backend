from django.db import models
from artgallery.storage_backends import BunnyStorage
import os

def hero_image_upload_to(instance, filename):
    return os.path.join("hero/images", filename)

class HeroImage(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(
        upload_to=hero_image_upload_to,
        storage=BunnyStorage(),
    )
    is_active = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"HeroImage {self.id}"
