from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^bars/',views.index,name = 'index'),
    url('^$', views.show_video, name='show_video'),
    url(r'^vid/', views.video_upload, name='video_upload'),
    #url(r'^audio/', views.audio_upload, name='audio_upload'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)