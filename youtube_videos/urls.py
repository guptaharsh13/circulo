from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import YouTubeVideoView

router = DefaultRouter()
router.register(prefix="", viewset=YouTubeVideoView, basename="youtube_videos")

urlpatterns = [
    path("", include(router.urls))
]
