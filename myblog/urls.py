from django.conf.urls import url #, patterns
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/draft/$', views.post_draft, name='post_draft'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/publish/(?P<pk>\d+)/$', views.post_publish, name='post_publish'),
    url(r'^post/delete/(?P<pk>\d+)/$', views.post_delete, name='post_delete'),
    url(r'^post/unpublish/(?P<pk>\d+)/$', views.post_unpublish, name='post_unpublish'),
    url(r'^post/edit/(?P<pk>\d+)/$', views.post_edit, name='post_edit'),
    url(r'^comment/new/(?P<pk>\d+)/$', views.comment_new, name='comment_new'),
    url(r'^comment/publish/(?P<pk>\d+)/$', views.comment_publish, name='comment_publish'),
    url(r'^comment/remove/(?P<pk>\d+)/$', views.comment_remove, name='comment_remove'),
    url(r'^comment/edit/(?P<pk>\d+)/$', views.comment_edit, name='comment_edit'),
]
