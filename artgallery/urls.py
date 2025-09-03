from rest_framework.routers import DefaultRouter
from artgallery.views import (
    HeroVideoViewSet,
    ArtworkViewSet,
    ArtworkImageViewSet,
    ArtworkVideoViewSet,
)

# --------------------------------------------------
# DRF Router setup
# Purpose:
#   - Automatically generates RESTful API routes
#   - Each registered ViewSet gets list/retrieve/create/update/delete endpoints
# --------------------------------------------------
router = DefaultRouter()

# Hero Video endpoints
#   /api/hero-videos/
#   /api/hero-videos/<id>/
router.register(r"hero-videos", HeroVideoViewSet, basename="hero-videos")

# Artwork endpoints
#   /api/artworks/
#   /api/artworks/<id>/
router.register(r"artworks", ArtworkViewSet, basename="artworks")

# Artwork Image endpoints
#   /api/artwork-images/
#   /api/artwork-images/<id>/
router.register(r"artwork-images", ArtworkImageViewSet, basename="artwork-images")

# Artwork Video endpoints
#   /api/artwork-videos/
#   /api/artwork-videos/<id>/
router.register(r"artwork-videos", ArtworkVideoViewSet, basename="artwork-videos")

# Expose all registered routes
urlpatterns = router.urls
