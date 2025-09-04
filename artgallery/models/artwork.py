from django.db import models

# --------------------------------------------------
# Artwork model
# Represents a single artwork entry
# --------------------------------------------------
class Artwork(models.Model):
    CATEGORY_CHOICES = [
        ("highlight", "Highlight"),
        ("recent", "Recent"),
        ("general", "General"),
    ]

    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="general")
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Artwork {self.id}"


# --------------------------------------------------
# ArtworkImage model
# Stores multiple images for an artwork
# --------------------------------------------------
class ArtworkImage(models.Model):
    artwork = models.ForeignKey(Artwork, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/artworks/")           # stored in Bunny
    height_cm = models.DecimalField(max_digits=6, decimal_places=2)   # manually entered by Linda
    width_cm = models.DecimalField(max_digits=6, decimal_places=2)    # manually entered by Linda
    order = models.PositiveSmallIntegerField(default=0)               # allows sorting
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.artwork.title or self.artwork.id}"


# --------------------------------------------------
# ArtworkVideo model
# Stores optional videos for an artwork (max 3)
# --------------------------------------------------
class ArtworkVideo(models.Model):
    artwork = models.ForeignKey(Artwork, related_name="videos", on_delete=models.CASCADE)
    video = models.FileField(upload_to="videos/artworks/")            # stored in Bunny
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Video for {self.artwork.title or self.artwork.id}"
