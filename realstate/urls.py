from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (
    homepage_view,
    list_view,
    realstate_detail_view,
    rs_delete_view,
    realstate_create_view,
    rs_update_view,
    realstate_hx_detail_view,
    realstate_imgs_hx_detail_view,
    rs_image_delete_view,
    search_view,
    advanced_search_view,


)
app_name="realstate"
urlpatterns = [
    path('homepage/',homepage_view,name="homepage"),
    path('my/realstate',list_view,name="list-view"),

    path('create/',realstate_create_view,name="rs-create"),
    
    
    path('hx/realstate/<int:parent_id>/images/<int:id>',
        realstate_imgs_hx_detail_view,name="hx-images-update"),
    path('hx/realstate/<int:parent_id>/images/',
        realstate_imgs_hx_detail_view,name="hx-images-new"),
    path('hx/realstate/<int:id>',realstate_hx_detail_view,name="hx-rs-detail"),

    path("update/<int:id>/",rs_update_view,name="rs-update"),


    path('realstate/<int:parent_id>/images/<int:id>/delete/',
        rs_image_delete_view,name="images-delete"),
    path('realstate/<int:id>/delete/',rs_delete_view,name='delete'),
    path('realstate/<int:id>',realstate_detail_view,name="rs-detail"),

    path("realstate/search/",search_view,name="search"),
    path("realstate/advanced_search/",advanced_search_view,name="advanced_search"),

    ] 
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


