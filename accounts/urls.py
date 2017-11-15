from django.conf.urls import url
from .views import logout, login

urlpatterns =[
    url(r'^logout', logout),
    url(r'^login', login),
    ]