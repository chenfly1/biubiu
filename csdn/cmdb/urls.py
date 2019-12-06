"""cmdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include,url
from django.contrib import admin
#from User.views import index,login
#from User import urls as user_urls
from asset import urls as asset_urls
from views import *

urlpatterns = [
    path(r'^admin/', include(admin.site.urls)),
    path(r'^user/', include(user_urls)),
    path(r'^asset/', include(asset_urls)),
    path(r'^login/', login),
    path(r'^logout/', logout),
    path(r'^settings/', user_settings),
    path(r'^update_userinfo/', update_userinfo),
    path(r'^$',index),
    path(r'^index/$',index),

]
