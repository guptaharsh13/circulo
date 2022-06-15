import requests
from datetime import datetime, timedelta, timezone
from django.conf import settings
from .models import YouTubeVideo, APICall
import os
import environ
from pathlib import Path


path = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(env_file=os.path.join(path, ".env"))


def parseItem(item):
    snippet = item.get("snippet")
    published_on = snippet.get("publishedAt")
    return {
        "video_title": snippet.get("title"),
        "video_description": snippet.get("description"),
        "published_on": datetime.strptime(published_on, "%Y-%m-%dT%H:%M:%SZ")
    }


def parseResponse(response):
    response = eval(response.content.decode())
    return list(map(parseItem, response.get("items")))


def makeRequest(query=settings.QUERY, published_after=None, page_token=None, api_key=None):
    if not api_key:
        return

    if not published_after:
        published_after = f"{(datetime.now(timezone.utc) - timedelta(seconds=settings.INTERVAL)).isoformat('T').replace('+00:00', '')}Z"

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
        return None

    if not response.status_code == 200:
        print("unable to make a successful request")
        print(response.content.decode())
        return None

    if not eval(response.content.decode()).get("nextToken"):
        return parseResponse(response=response)

    temp_response = makeRequest(
        query=query, published_after=published_after, page_token=page_token)

    return parseResponse(response=response) + parseResponse(response=temp_response)


def saveVideos(videos_json):

    count = 0

    if not videos_json:
        APICall.objects.create()
        return count

    videos = []
    for video in videos_json:
        count += 1
        videos.append(YouTubeVideo(**video))

    YouTubeVideo.objects.bulk_create(videos)
    APICall.objects.create(number_of_videos=count)
    return count


def useAPIKeys():

    api_keys = env("API_KEYS")
    api_keys = api_keys.replace(" ", "").split(",")

    api_calls = APICall.objects.order_by("-made_on")
    published_after = None

    if api_calls.exists():

        if api_calls[0].number_of_videos < settings.THRESHOLD:
            print("skipped")
            return 0

        made_on = api_calls[0].made_on
        published_after = f"{made_on.isoformat('T').replace('+00:00', '')}Z"

    for api_key in api_keys:
        videos = makeRequest(published_after=published_after, api_key=api_key)
        if videos is None:
            continue
        return saveVideos(videos_json=videos)

    return 0
