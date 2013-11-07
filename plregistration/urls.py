from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
    (r'attachments/', include('attachments.urls')),
    (r'^', include('lbforum.urls')),
)
