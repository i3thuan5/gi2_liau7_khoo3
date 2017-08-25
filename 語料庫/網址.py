# -*- coding: utf-8 -*-
from django.conf.urls import url
from 語料庫.介面 import 傳音檔

urlpatterns = [
    url(r'^音檔/(?P<音檔編號>\d+)/(?P<開始時間>[\d\.]+)/(?P<結束時間>[\d\.]+)$', 傳音檔),
]
