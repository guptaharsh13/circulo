from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import YouTubeVideo


@receiver(post_save, sender=YouTubeVideo)
def my_handler(sender, instance, **kwargs):
    instance.indexing()
