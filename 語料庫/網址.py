# -*- coding: utf-8 -*-
from django.conf.urls import url
from 語料庫.介面 import 傳音檔
from 校對工具.views import 工具
from django.http.response import JsonResponse

_工具 = 工具()


def 標本調(request, 漢字, 臺羅):
    return JsonResponse({'本調': _工具.標本調(漢字, 臺羅)})


urlpatterns = [
    url(
        r'^音檔/(?P<音檔編號>\d+)/(?P<開始時間>[\d\.]+)/(?P<結束時間>[\d\.]+)/audio.wav$',
        傳音檔
    ),
    url(
        r'^標本調/(?P<漢字>[^/]+)/(?P<臺羅>.+)$',
        標本調
    ),
]
