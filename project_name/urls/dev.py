import debug_toolbar
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

from {{ project_name }}.urls import urlpatterns as base_urlpatterns


urlpatterns = base_urlpatterns
urlpatterns += [
    url(r'^__debug__/', include(debug_toolbar.urls)),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
