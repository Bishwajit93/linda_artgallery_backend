from django.contrib import admin
from .models.image import Image
from .models.video import Video
# Add other models here as you create them

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at")
    search_fields = ("title",)

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at")
    search_fields = ("title",)
