from django.contrib import admin
from artgallery.models.herovideo import HeroVideo
from artgallery.models.artwork import Artwork, ArtworkImage, ArtworkVideo


# --------------------------------------------------
# HeroVideo admin (simple, no inline needed)
# --------------------------------------------------
@admin.register(HeroVideo)
class HeroVideoAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "order", "is_active", "created_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("title", "description")
    ordering = ("order", "-created_at")


# --------------------------------------------------
# Inline setup: ArtworkImage + ArtworkVideo inside Artwork
# --------------------------------------------------
class ArtworkImageInline(admin.TabularInline):  # Could also be StackedInline
    model = ArtworkImage
    extra = 1  # show 1 empty form by default
    fields = ["image", "height_cm", "width_cm", "order", "uploaded_at"]
    readonly_fields = ["uploaded_at"]
    ordering = ("order", "-uploaded_at")


class ArtworkVideoInline(admin.TabularInline):  # Could also be StackedInline
    model = ArtworkVideo
    extra = 1
    fields = ["video", "uploaded_at"]
    readonly_fields = ["uploaded_at"]
    ordering = ("-uploaded_at",)


# --------------------------------------------------
# Artwork admin (with inline children)
# --------------------------------------------------
@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "is_published", "created_at")
    list_filter = ("category", "is_published", "created_at")
    search_fields = ("title", "description")
    ordering = ("-created_at",)

    # Attach inlines so Linda manages images/videos directly in Artwork form
    inlines = [ArtworkImageInline, ArtworkVideoInline]
