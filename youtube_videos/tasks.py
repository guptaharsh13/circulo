from celery import shared_task
import time


@shared_task(bind=True)
def fetchYouTubeVideos(self):
    time.sleep(5)
    print("Have called the YouTube API")
    return "done"
