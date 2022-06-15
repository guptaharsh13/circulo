from django.contrib import admin
from .models import YouTubeVideo, APICall


class YouTubeVideoAdmin(admin.ModelAdmin):
    list_display = ("id", "video_title", "published_on")
    list_display_links = ("id", "video_title")
    list_filter = ("published_on",)
    search_fields = ("id", "video_title", "video_description")


class APICallAdmin(admin.ModelAdmin):
    list_display = ("id", "number_of_videos", "made_on")
    list_display_links = ("id", "number_of_videos")
    list_filter = ("number_of_videos", "made_on")
    search_fields = ("id", "number_of_videos", "made_on")


# Register your models here.
admin.site.register(YouTubeVideo, YouTubeVideoAdmin)

admin.site.register(APICall, APICallAdmin)
