from django.conf.urls import patterns, include, url
from django.contrib import admin
from jib_site import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'jib_site.views.home', name='home'),
    url(r'^login/$', 'jib_auth.views.login'),
    url(r'^trans/(\d+)/', 'financial.views.trans'),
    url(r'^groups/(.+)/', 'groups.views.groups'),
    url(r'^group/(.+)/', 'groups.views.group'),
    url(r'^register/$', 'jib_auth.views.register'),
    url(r'^upgrade/$', 'jib_auth.views.upgrade'),
    # url(r'^jib_site/', include('jib_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
     (r'^mymedia/(?P<path>.*)$', 'django.views.static.serve', 
	     {'document_root':     settings.MEDIA_ROOT}),
)

