import json
import os
from rest_framework.response import Response
from rest_framework.views import APIView
from elasticsearch_dsl import connections
import django_filters.rest_framework
from .models import YouTubeVideo
from .serializers import YouTubeVideoSerializer
from .doc_type import YouTubeVideoDoc


class YouTubeVideoSearchView(APIView):
    def get(self, request):
        query = request.query_params.get('q')
        ids = []
        if query:
            try:
                s = YouTubeVideoDoc.search()
                s = s.query('match', name=query)
                response = s.execute()
                response_dict = response.to_dict()
                hits = response_dict['hits']['hits']
                ids = [hit['_source']['id'] for hit in hits]
                queryset = YouTubeVideo.objects.filter(id__in=ids)
                youtube_video_list = list(queryset)
                youtube_video_list.sort(
                    key=lambda youtube_video: ids.index(youtube_video.id))
                serializer = YouTubeVideoSerializer(
                    youtube_video_list, many=True)
            except Exception as e:
                youtube_videos = YouTubeVideo.objects.filter(
                    name__icontains=query)
                serializer = YouTubeVideoSerializer(youtube_videos, many=True)
            return Response(serializer.data)
