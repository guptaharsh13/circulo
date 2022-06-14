from django.contrib import admin
from django.urls import path
from .views import index
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny


schema_view = get_schema_view(
    openapi.Info(
        title="Circulo",
        default_version='v1.0.0',
        description="Backend Assignment | FamPay",
        contact=openapi.Contact(email="hg242322@gmail.com"),
    ),
    public=True,
    permission_classes=[AllowAny],

)

urlpatterns = [

    path('admin/', admin.site.urls),
    path("", view=index, name="index"),

    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),

]
