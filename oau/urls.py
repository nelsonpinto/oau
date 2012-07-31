from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'company.views.home'),    
    url(r'^company/$', 'company.views.index'),
    url(r'^user/createaccount/$', 'company.views.user_createaccount'),
    url(r'^user/signin/$', 'company.views.user_signin'),
    url(r'^user/signout/$', 'company.views.user_signout'),
    url(r'^user/private/$', 'company.views.user_private'),
    url(r'^proyects/$', 'proyects.views.index'),
    url(r'^store/$', 'store.views.index'),
        
    # Examples:
    #url(r'^$', 'oau.views.home', name='home'),
    #url(r'^oau/', include('oau.foo.urls')),
    #url(r'^$', '{{ project_name }}.views.home', name='home'),
    #url(r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
        
    )