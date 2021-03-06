# Blogapp URLS
from django.conf.urls import url
from .views import blogapp, viewpost, newpost, editpost, addcomment

urlpatterns =[
    url(r'^$', blogapp, name='blogapp'),
    url(r'^posts/(\d+)$', viewpost, name='viewpost'),
    url(r'^posts/add', newpost, name='newpost'),
    url(r'^posts/(\d+)/edit', editpost, name='editpost'),
    url(r'^posts/(\d+)/comments/add$', addcomment, name='addcomment'),
    ]