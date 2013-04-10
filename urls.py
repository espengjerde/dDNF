from django.conf.urls.defaults import *
from login import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    url(r'^meta/$',views.checkmeta),    
    url(r'^stats/$', views.statistics),
    #url(r'^',views.checkmeta),
    url(r'^',views.login),
    
    # (r'^dDNF/', include('dDNF.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)

