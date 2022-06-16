from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import YouTubeVideoView
from .elastic_views import YouTubeVideoSearchView


router = DefaultRouter()
router.register(prefix="", viewset=YouTubeVideoView, basename="youtube_videos")

urlpatterns = [
    path("", include(router.urls)),
    path("elastic", YouTubeVideoSearchView.as_view(), name="elastic_search")
]
