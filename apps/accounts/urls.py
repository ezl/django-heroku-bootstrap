from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to, direct_to_template


urlpatterns = patterns('accounts.views',
    url(r'^settings/$', 'user_settings', name='user_settings'),
    url(r'^signup/$', 'signup', name='signup'),
    url(r'', include('django.contrib.auth.urls')),
)
