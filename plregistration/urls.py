from django.conf.urls import patterns, include, url
from django.conf import settings

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from registration.views import register
from lbforum.accountviews import profile
import captcha

urlpatterns = patterns('',
    url(r'^accounts/register/$',
        register,
        { 'backend': 'plregistration.backends.PlBackends' },
        name='registration_register'),
    url(r'^user/(?P<user_id>\d+)/$', profile, name='user_profile'),
    url(r'^accounts/', include('registration.backends.default.urls')),

    (r'^attachments/', include('attachments.urls')),
    #url(r'^captcha/', include('captcha.urls')),
    (r'^', include('lbforum.urls')),
)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
