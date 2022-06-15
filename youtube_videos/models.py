from django.db import models
from datetime import datetime

# Create your models here.


class YouTubeVideo(models.Model):

    video_title = models.CharField(max_length=255)
    video_description = models.TextField()
    published_on = models.DateTimeField()

    # to track the time when the entry is created in the database
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.video_title} | {self.published_on}"


class APICall(models.Model):
    date_time = models.DateTimeField(default=datetime.now)
    number_of_videos = models.PositiveBigIntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.date_time} | {self.number_of_videos}"

    class Meta:
        ordering = ("-date_time",)
