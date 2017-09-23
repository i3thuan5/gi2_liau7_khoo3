# -*- coding: utf-8 -*-
from django.conf.urls import url
from 校對工具.介面 import 標本調


urlpatterns = [
    url(
        r'^標本調/(?P<漢字>[^/]+)/(?P<臺羅>.+)$',
        標本調
    ),
]
