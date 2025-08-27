from django.db import models
from cloudinary.models import CloudinaryField

class Image(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    # Dimensions (unit not enforced, Linda decides)
    height = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    width = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    depth = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

    image = CloudinaryField(
        "image",
        resource_type="image",
        folder="linda_artgallery/images/artworks",
    )


    is_published = models.BooleanField(default=False)
    order = models.PositiveSmallIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ["order", "-created_at"]
        db_table = "gallery_image"

    def __str__(self):
        return self.title or f"Image #{self.pk}"
