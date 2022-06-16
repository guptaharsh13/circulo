import time
import os
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from elasticsearch_dsl import Search, Index, connections
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from youtube_videos.models import YouTubeVideo
from youtube_videos.doc_type import YouTubeVideoDoc


class Command(BaseCommand):
    help = 'Indexes YouTubeVideo in Elastic Search'

    def handle(self, *args, **options):
        es = Elasticsearch(
            [{'host': settings.ES_HOST, 'port': settings.ES_PORT}],
            index="youtube_video"
        )
        youtube_video_index = Index('youtube_videos', using='art')
        youtube_video_index.doc_type(YouTubeVideoDoc)
        if youtube_video_index.exists():
            youtube_video_index.delete()
            print('Deleted youtube_video index.')
        YouTubeVideoDoc.init()
        result = bulk(
            client=es,
            actions=(youtube_video.indexing()
                     for youtube_video in YouTubeVideo.objects.all().iterator())
        )
        print('Indexed youtube_video.')
        print(result)
