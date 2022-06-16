import requests
from datetime import datetime, timezone, timedelta
from django.utils.timezone import utc
from django.conf import settings
from .models import YouTubeVideo, APICall
import os
import environ
from pathlib import Path
from django_celery_beat.models import PeriodicTask


path = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(env_file=os.path.join(path, ".env"))


def parseItem(item):
    snippet = item.get("snippet")
    published_on = snippet.get("publishedAt")
    video_title = snippet.get("title")
    video_title = video_title.encode(
        "utf-8", "ignore").decode("utf-8", "surrogateescape")

    # because 'utf-8' codec can't encode characters: surrogates not allowed
    # Thus, I have ignored surrogate characters

    return {
        "video_id": item.get("id").get("videoId"),
        "video_title": video_title,
        "video_description": snippet.get("description"),
        "thumbnail_url": snippet.get("thumbnails").get("default").get("url"),

        # Django uses time-zone-aware datetime objects. Thus, we are performing this conversion
        "published_on": datetime.strptime(published_on, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=utc)
    }


def parseResponse(response):
    response = eval(response.content.decode())
    return list(map(parseItem, response.get("items")))


def makeRequest(query=settings.QUERY, published_after=None, page_token=None, api_key=None):
    if not api_key:
        return

    if not published_after:
        # published_after = f"{(datetime.now(timezone.utc) - timedelta(seconds=settings.INTERVAL)).isoformat('T').replace('+00:00', '')}Z"
        published_after = "2022-06-16T09:04:54.943341Z"

    params = {"part": "snippet",
              "maxResults": 50,
              "order": "date",
              "q": query,
              "type": "video",
              "publishedAfter": published_after,
              "key": api_key
              }

    if page_token:
        params["pageToken"] = page_token

    response = requests.get(
        url="https://www.googleapis.com/youtube/v3/search",
        params=params
    )

    if response.status_code == 403:
        print("invalid API key or unauthorized or quota exceeded on API key, use next API key, otherwise return")
        return

    if not response.status_code == 200:
        print("unable to make a successful request")
        return

    next_token = eval(response.content.decode()).get("nextPageToken")

    if not next_token:
        return parseResponse(response=response)

    temp_response = makeRequest(
        query=query, published_after=published_after, page_token=next_token, api_key=api_key)

    return parseResponse(response=response) + temp_response


def saveVideos(videos_json):

    count = 0

    videos = []
    for video in videos_json:
        count += 1
        videos.append(YouTubeVideo(**video))

    YouTubeVideo.objects.bulk_create(videos)
    return count


def updateInterval(factor):
    task = PeriodicTask.objects.filter(name="fetch_youtube_videos")
    if not task.exists():
        return False
    task = task.first()
    interval = task.interval
    value = min(settings.MAX_INTERVAL, interval.every * factor)
    value = max(settings.MIN_INTERVAL, value)
    interval.every = value
    interval.save()
    return True


def useAPIKeys():

    api_keys = env("API_KEYS")
    api_keys = api_keys.replace(" ", "").split(",")

    api_calls = APICall.objects.order_by("-made_on")
    published_after = None

    if api_calls.exists():
        made_on = api_calls[0].made_on
        published_after = f"{made_on.isoformat('T').replace('+00:00', '')}Z"

    count = 0
    for api_key in api_keys:
        videos = makeRequest(published_after=published_after, api_key=api_key)
        if videos is None:
            continue
        count = saveVideos(videos_json=videos)

    APICall.objects.create(number_of_videos=count)

    factor = settings.MULTIPLICATION_FACTOR
    if count > settings.THRESHOLD:
        factor = 1/settings.MULTIPLICATION_FACTOR

    updateInterval(factor=factor)
    return count
