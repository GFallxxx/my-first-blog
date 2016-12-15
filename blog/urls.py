"""mysite URL Configuration

    ^ for the beginning of the text
    $ for the end of the text
    \d for a digit
    + to indicate that the previous item should be repeated at least once
    () to capture part of the pattern

p.es. 
    http://www.mysite.com/post/12345/
    ^post/(\d+)/$

"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/tobepublished/$', views.post_tobepublished, name='post_tobepublished'),
    url(r'^post/publish/(?P<pk>\d+)/$', views.post_publish, name='post_publish'), 
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/remove/(?P<pk>\d+)/$', views.post_remove, name='post_remove'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
]
