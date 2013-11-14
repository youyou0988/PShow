from django.conf.urls import patterns, include, url
from os.path import dirname, join

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
media = join(
    dirname(dirname(__file__)), 'media'
)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pshow.views.home', name='home'),
    # url(r'^pshow/', include('pshow.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.main'),
    
    # for register and login/logout
    url(r'^register/$', 'main.views.register_'),
    url(r'^login/$', 'main.views.login_'),
    url(r'^logout/$', 'main.views.logout_'),
    
    # for show
    url(r'^show/$', 'show.views.show_'),
    
    # for check
    url(r'^check/$', 'check.views.check_'),
    url(r'^add_algorithm/$', 'check.views.add_algorithm'),
    url(r'^udpate_algorithm/(?P<index>\d+)/$', 'check.views.update_algorithm'),
    
    # for show
    url(r'^show/action/$', 'show.views.action'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':media}),
    
    # for info
    url(r'^info/$', 'info.views.info'),
    
)
