from __future__ import absolute_import, unicode_literals
from celery import Celery
import os
import environ
from pathlib import Path
from django.conf import settings
from celery.schedules import crontab
from datetime import timedelta

path = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(env_file=os.path.join(path, ".env"))

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      f'circulo.settings.{env("django_env")}')

app = Celery("circulo")
app.conf.enable_utc = False
app.conf.update(timezone="Asia/Kolkata")

app.config_from_object(settings, namespace="CELERY")

# app.conf.beat_schedule = {}

app.conf.beat_schedule = {
    "fetch_youtube_videos": {
        "task": "youtube_videos.tasks.fetchYouTubeVideos",
        "schedule": timedelta(seconds=settings.INTERVAL)
    }
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
