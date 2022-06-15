from .models import YouTubeVideo
from .serializers import YouTubeVideoSerializer
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.throttling import ScopedRateThrottle
from .pagination import YouTubeVideoPagination

# Create your views here.


class YouTubeVideoView(ListModelMixin, RetrieveModelMixin, GenericViewSet):

    queryset = YouTubeVideo.objects.all()
    serializer_class = YouTubeVideoSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("video_title", "video_description")
    ordering_fields = ("published_on",)
    ordering = ("-published_on")
    throttle_classes = (ScopedRateThrottle,)
    throttle_scope = "youtube_videos"
    pagination_class = YouTubeVideoPagination
