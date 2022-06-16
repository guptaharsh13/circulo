from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from .views import index
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

admin.site.site_title = 'círculo'
admin.site.site_header = 'círculo Admin Panel'
admin.site.index_title = 'Welcome to círculo Admin Panel'


schema_view = get_schema_view(
    openapi.Info(
        title="círculo",
        default_version='v1.0.0',
        description="Backend Assignment | FamPay",
        contact=openapi.Contact(email=settings.DEFAULT_FROM_EMAIL)
    ),
    public=True,
    permission_classes=[AllowAny],

)

urlpatterns = [

    path('admin/', admin.site.urls),
    path("", view=index, name="index"),
    path("youtube-videos", include("youtube_videos.urls")),

    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),

]
