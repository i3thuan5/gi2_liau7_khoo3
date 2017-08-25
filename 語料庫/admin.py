
from django.contrib import admin
from django.contrib.auth.models import User, Group
# from django.contrib.sites.models import Site
from 語料庫.models import 語料表
from 語料庫.models import 音檔表
from 語料庫.models import 語料狀況表
from django.template.response import TemplateResponse
from django.conf.urls import url
from django.db import models
from django.forms.widgets import TextInput, CheckboxSelectMultiple

admin.site.unregister(User)
admin.site.unregister(Group)

# admin.site.unregister(Site)

admin.site.disable_action('delete_selected')


class 語料表管理(admin.ModelAdmin):
    list_display = ['id', '音檔', '漢字', '本調臺羅', '口語調臺羅', '對齊狀態']
    ordering = ['id']
    list_filter = ['音檔__類別', 'sing5hong5有揀出來用無', '語料狀況', ]

    search_fields = [
        '漢字', '本調臺羅', '口語調臺羅',
        'sing5hong5舊編號', 'sing5hong5新編號',
    ]
    fieldsets = (
        ('音檔', {
            'fields': ('音檔', ),
            'classes': ['wide']
        }),
        (None, {
            'fields': ('語料狀況', ),
            'classes': ['wide']
        }),
        #         (None, {
        #             'fields': ('聲音開始時間', '聲音結束時間', ),
        #             'classes': ['wide']
        #         }),
        (None, {
            'fields': ('漢字', '本調臺羅', '口語調臺羅', ),
            'classes': ['wide']
        }),
    )

    actions = [
        '設定類別_教材',
    ]

    # 文字欄位顯示從textarea改成input
    # 多對多欄位改用複選
    formfield_overrides = {
        models.TextField: {'widget': TextInput(attrs={'size': 80})},
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

    def 設定類別_教材(self, request, queryset):
        queryset.update(類別='S1')

    change_form_template = 'admin/gi2_liau7_khoo3/語料表/custom_change_form.html'

    def get_urls(self):
        urls = super(語料表管理, self).get_urls()
        my_urls = [
            url(r'^語料表/$', self.admin_site.admin_view(self.my_view))
        ]
        return my_urls + urls

    def my_view(self, request):
        # ...
        context = dict(
            # Include common variables for rendering the admin template.
            self.admin_site.each_context(request),
            # Anything else you want in the context...
            #            key=value,
        )
        return TemplateResponse(
            request,
            'admin/gi2_liau7_khoo3/語料表/custom_change_form.html',
            context
        )

    def has_add_permission(self, request):
        # 薛：只能由程式上傳音檔和語料
        # 薛：任何人都不能從後台新增
        return False


class 音檔表管理(admin.ModelAdmin):
    list_display = ['id', '資料夾名', '聲音檔名', '聽拍檔名']
    ordering = ['資料夾名', '聲音檔名', '聽拍檔名']

    def has_add_permission(self, request):
        # 薛：只能由程式上傳音檔和語料
        # 薛：任何人都不能從後台新增
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(語料狀況表)
admin.site.register(音檔表, 音檔表管理)
admin.site.register(語料表, 語料表管理)
