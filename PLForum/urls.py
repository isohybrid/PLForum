from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from registration.views import register
from lbforum.accountviews import profile

from views import show_page, show_page2, show_carousel

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    ##url(r'^$', 'PLForum.views.home', name='home'),
    ##url(r'^PLForum/', include('PLForum.foo.urls')),
    url(r'^accounts/register/$', 
        register,
        { 'backend': 'plregistration.backends.simple.PlBackends' },
        name='registration_register'),
    # a problem come out here.
    ##url(r'^user/(?P<user_id)\d+)/$', profile, name='user_profile'),

    (r'^accounts/', include('registration.backends.default.urls')),
    # url(r'^captcha/', include('captcha.urls')),
    # (r'^admin/', include(admin.site.urls)),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^attachments/', include('attachments.urls')),
    (r'^', include('lbforum.urls')),
    ###url(r'^forum/', include('plregistration.urls')),

    ###url(r'^page/', show_page),
    ###url(r'^carousel/', show_page2, name="carousel"),
    url(r'^carousel/', show_carousel, name="carousel"),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
