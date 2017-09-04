
from django.contrib import admin
from 語料庫.models import 語料表
from 語料庫.models import 語料狀況表
from django.db import models
from django.forms.widgets import TextInput, CheckboxSelectMultiple
from 語料庫.widgets.ReadOnlyAdminFields import ReadOnlyAdminFields


admin.site.disable_action('delete_selected')


class 語料表管理(ReadOnlyAdminFields, admin.ModelAdmin):
    list_display = ['id', '音檔', '漢字', '本調臺羅', '口語調臺羅', '對齊狀態', '校對者', '校對時間']
    ordering = ['校對者', 'id']
    list_filter = ['音檔__類別', '語料狀況', '校對者']

    readonly_fields = ('音檔',)
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
        (None, {
            'fields': ('漢字', '本調臺羅', '口語調臺羅', '備註', ),
            'classes': ['wide']
        }),
    )

    # 文字欄位顯示從textarea改成input
    # 多對多欄位改用複選
    formfield_overrides = {
        models.TextField: {'widget': TextInput(attrs={'size': 80})},
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

    change_form_template = 'admin/gi2_liau7_khoo3/語料表/custom_change_form.html'

    def save_model(self, request, obj, form, change):
        # 儲存校對者
        obj.校對者 = request.user
        super(語料表管理, self).save_model(request, obj, form, change)

    def has_add_permission(self, request):
        # 薛：只能由程式上傳音檔和語料
        # 薛：任何人都不能從後台新增
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_queryset(self, request):
        qs = super(語料表管理, self).get_queryset(request)
        return qs.filter(sing5hong5有揀出來用無=True)

    class Media:
        css = {
            "all": ("css/admin_gi2_liau7_pio2.css",)
        }
#     actions = [
#         '設定類別_教材',
#     ]
#
#     def 設定類別_教材(self, request, queryset):
#         queryset.update(類別='S1')


admin.site.register(語料表, 語料表管理)
admin.site.register(語料狀況表)
