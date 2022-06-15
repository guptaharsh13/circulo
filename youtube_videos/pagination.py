from rest_framework.pagination import CursorPagination


class YouTubeVideoPagination(CursorPagination):
    page_size = 5
    ordering = "-published_on"
