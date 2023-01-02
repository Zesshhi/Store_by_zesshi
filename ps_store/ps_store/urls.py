from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('store.urls')),

    path('cart/', include('cart.urls')),

    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('adminskaya_zalupa_krota_1x1_zxc_sf/', admin.site.urls),

]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)