from django.apps import AppConfig
from django.conf import settings
from elasticsearch_dsl import connections


class YoutubeVideosConfig(AppConfig):
    name = 'youtube_videos'

    def ready(self):
        import youtube_videos.signals
        try:
            connections.create_connection(
                'art',
                hosts=[{'host': settings.ES_HOST, 'port': settings.ES_PORT}])
        except Exception as e:
            print(e)
