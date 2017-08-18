
from django.contrib import admin
from django.contrib.auth.models import User, Group
# from django.contrib.sites.models import Site
from 語料庫.models import 語料表
from 語料庫.models import 音檔表

admin.site.unregister(User)
admin.site.unregister(Group)

# admin.site.unregister(Site)

admin.site.disable_action('delete_selected')


class 語料表管理(admin.ModelAdmin):
    list_display = ['id', '類別', '漢字', '書寫', '對齊狀態', ]
    ordering = ['-id']
    list_filter = ['音檔__類別', '漢字', ]

    actions = [
        '設定類別_教材',
    ]

    def 設定類別_教材(self, request, queryset):
        queryset.update(類別='S1')


admin.site.register(音檔表)
admin.site.register(語料表, 語料表管理)
