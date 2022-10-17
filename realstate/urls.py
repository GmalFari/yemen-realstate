from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (
    realstate_create_view,
     realstate_detail_view,
     homepage_view,
     list_view,
     rs_update_view,
     realstate_hx_detail_view,

)
app_name="realstate"
urlpatterns = [
    path('homepage',homepage_view,name="homepage"),
    path('my/realstate',list_view,name="list-view"),
    path('create',realstate_create_view,name="rs-create"),
    path("update/<int:id>",rs_update_view,name="rs-update"),
    path('hx/realstate/<int:id>',realstate_hx_detail_view,name="hx-rs-detail"),
    path('realstate/<int:id>',realstate_detail_view,name="rs-detail"),
    ] 
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


