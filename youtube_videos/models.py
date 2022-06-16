import django
from django.db import models
from django.contrib.postgres.indexes import BrinIndex

# Create your models here.


class YouTubeVideo(models.Model):

    video_id = models.CharField(max_length=12)
    video_title = models.CharField(max_length=255, db_index=True)
    video_description = models.TextField(db_index=True)
    thumbnail_url = models.URLField()
    published_on = models.DateTimeField()

    def __str__(self):
        return f"{self.video_title} | {self.published_on}"

    class Meta:
        ordering = ("-published_on",)
        indexes = (
            BrinIndex(fields=("published_on",)),
        )


class APICall(models.Model):
    made_on = models.DateTimeField(auto_now_add=True)
    number_of_videos = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.made_on} | {self.number_of_videos}"

    class Meta:
        ordering = ("-made_on",)
        indexes = (
            BrinIndex(fields=("made_on",)),
        )
