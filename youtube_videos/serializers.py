from rest_framework.serializers import ModelSerializer
from .models import YouTubeVideo


class YouTubeVideoSerializer(ModelSerializer):
    class Meta:
        model = YouTubeVideo
        fields = "__all__"
