from django.conf.urls import include, url #, patterns
from django.contrib.auth import views
from django.contrib import admin
#from . import views

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    #url(r'', include('blog.urls')),
    #url(r'^myblog/', include('myblog.urls')),
    url(r'', include('myblog.urls')),
]
