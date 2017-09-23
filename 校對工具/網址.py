# -*- coding: utf-8 -*-
from django.conf.urls import url
from 校對工具.介面 import 標本調
from 校對工具.介面 import 口語標漢字本調


urlpatterns = [
    url(
        r'^標本調/(?P<漢字>[^/]+)/(?P<臺羅>.+)$',
        標本調
    ),
    url(
        r'^口語標漢字本調/(?P<口語>.+)$',
        口語標漢字本調
    ),
]
