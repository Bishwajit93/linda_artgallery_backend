from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError
from .models import Image, Video

# ------------------------
# Admin for Image
# ------------------------
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_published", "order", "created_at")
    list_filter = ("is_published", "created_at")
    search_fields = ("title", "description")
    ordering = ("order", "-created_at")


# ------------------------
# Custom form for Video
# ------------------------
class VideoAdminForm(forms.ModelForm):
    # (unchanged)
    class Meta:
        model = Video
        fields = "__all__"
    def clean_video(self):
        f = self.cleaned_data.get("video")
        ct = getattr(f, "content_type", None)
        if ct and not ct.startswith("video/"):
            raise forms.ValidationError("Please upload a video file (mp4, mov, webm, mkv, m4v, avi).")
        return f


# ------------------------
# Admin for Video
# ------------------------
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    form = VideoAdminForm
    list_display = ("id", "title", "is_published", "order", "created_at")
    list_filter = ("is_published", "created_at")
    search_fields = ("title", "description")
    ordering = ("order", "-created_at")