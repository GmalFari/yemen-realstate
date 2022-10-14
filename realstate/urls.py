from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (
    realstate_create_view,
     realstate_detail_view,
     homepage_view,
)
app_name="realstate"
urlpatterns = [
    path('homepage',homepage_view,name="homepage"),
    path('create',realstate_create_view,name="rs-create"),
    path('realstate/<int:id>',realstate_detail_view,name="rs-detail"),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
