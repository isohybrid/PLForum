from django.conf.urls import patterns, include, url
from views import show_page, show_page2

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PLForum.views.home', name='home'),
    # url(r'^PLForum/', include('PLForum.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^attachments/', include('attachments.urls')),
    (r'^', include('lbforum.urls')),

    url(r'^page/', show_page),
    url(r'^page2/', show_page2),
)
