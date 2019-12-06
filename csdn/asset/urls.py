#coding:utf-8
from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^desktop/', desktop),
    url(r'^desktop_register/', desktop_register),
    url(r'^desktop_info/(\d{1,4})$', desktop_info),
    url(r'^desktops_upload_file/', desktops_upload_file),
    url(r'^desktops_downlload_excelmodels/', desktops_downlload_excelmodels),
    url(r'^desktops_download_alldata/', desktops_download_alldata),
    url(r'^sn_valid/', sn_valid),
]