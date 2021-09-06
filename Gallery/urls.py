from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^$', views.index, name='home'), 
    re_path(r'^search/', views.search_photo_category, name='search_results'), 
    re_path(r'^location/', views.location, name='locate')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)