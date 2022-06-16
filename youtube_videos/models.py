from django.db import models
from django.contrib.postgres.indexes import BrinIndex
from .doc_type import YouTubeVideoDoc

# Create your models here.


class YouTubeVideo(models.Model):

    video_title = models.CharField(max_length=255)
    video_description = models.TextField()
    published_on = models.DateTimeField()

    def __str__(self):
        return f"{self.video_title} | {self.published_on}"

    class Meta:
        ordering = ("-published_on",)
        indexes = (
            BrinIndex(fields=("published_on",)),
        )

    def indexing(self):
        doc = YouTubeVideoDoc(
            meta={'id': self.id},
            video_title=self.video_title,
            id=self.id
        )
        doc.save()
        return doc.to_dict(include_meta=True)


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
