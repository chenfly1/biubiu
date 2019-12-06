#coding:utf-8
from django.conf.urls import url
#from views import *
urlpatterns = [
    url(r'^validphone/$', valid_phone),
    url(r'^register/$', register),
    url(r'^phone_valid/$', phone_valid),
    url(r'^username_valid/$', username_valid),
    url(r'^email_valid/$', email_valid),
]