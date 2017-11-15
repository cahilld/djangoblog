from django.conf.urls import url
from .views import logout, login, register, profile

urlpatterns =[
    url(r'^logout', logout),
    url(r'^login', login),
    url(r'^register', register),
    url(r'^profile', profile)
    ]