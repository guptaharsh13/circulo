from django.contrib import admin
from .models import YoutubeVideo


class YoutubeVideoAdmin(admin.ModelAdmin):
    list_display = ("id", "video_title", "published_on",
                    "created_on", "updated")
    list_display_links = ("id", "video_title")
    list_filter = ("published_on", "created_on", "updated")
    search_fields = ("id", "video_title", "video_description")


# Register your models here.
admin.site.register(YoutubeVideo, YoutubeVideoAdmin)
