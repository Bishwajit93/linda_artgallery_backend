from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from artgallery.views import (
    PublishedImageViewSet, AdminImageViewSet,
    PublishedVideoViewSet, AdminVideoViewSet,
)
from artgallery.views import ping
from artgallery.views.upload_sign import sign_upload
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
# Public read-only
router.register(r"images", PublishedImageViewSet, basename="image")
router.register(r"videos", PublishedVideoViewSet, basename="video")
# Admin CRUD (login first in /admin)
router.register(r"admin/images", AdminImageViewSet, basename="admin-images")
router.register(r"admin/videos", AdminVideoViewSet, basename="admin-videos")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("ping/", ping),   # ✅ health check
    path("api/", include(router.urls)),
    path("api/uploads/sign/", sign_upload),
    
    # JWT
    path("api/auth/login", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/refresh", TokenRefreshView.as_view(), name="token_refresh"),
]
