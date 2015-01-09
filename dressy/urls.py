from django.conf.urls import patterns, include, url

from django.contrib import admin
from dressy import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dressy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'dressy.views.index'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/','home.views.index'),	
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', include('home.urls')),
    url(r'^Analytics/', include ('Analytics.urls')),
    url(r'^login/','home.views.login'),
    url(r'^logout/', 'home.views.logout'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
)
