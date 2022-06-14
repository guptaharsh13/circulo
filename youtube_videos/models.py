from django.db import models

# Create your models here.


class YoutubeVideo(models.Model):

    video_title = models.CharField(max_length=255)
    video_description = models.TextField()
    published_on = models.DateTimeField()

    # to track the time when the entry is created in the database
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.video_title} | {self.published_on}"
