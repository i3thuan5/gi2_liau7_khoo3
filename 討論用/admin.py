from django.contrib import admin
from 語料庫.管理.校對 import 校對表
from 語料庫.管理.校對 import 校對表管理
from 語料庫.models import 語料狀況表


def 註冊():
    for 狀況 in 語料狀況表.objects.all():
        class 狀態表(校對表):

            class Meta:
                proxy = True
                verbose_name = str(狀況)
                verbose_name_plural = verbose_name

        class 狀態管理(校對表管理):
            list_filter = ['音檔__類別', '校對者']

            def get_queryset(self, request):
                qs = super(狀態管理, self).get_queryset(request)
                return qs.filter(語料狀況=狀況)

        admin.site.register(狀態表, 狀態管理)
註冊()
