from django.contrib import admin
from django.db import models
from django.db.models.query_utils import Q
from django.forms.widgets import CheckboxSelectMultiple, Textarea
from django.utils.timezone import now
from 語料庫.widgets.ReadOnlyAdminFields import ReadOnlyAdminFields
from 語料庫.models import 語料表


class 校對表(語料表):

    def save(self, *args, **kwargs):
        self.校對時間 = now()
        super().save(*args, **kwargs)

    class Meta:
        proxy = True
        verbose_name = "1.校對表"
        verbose_name_plural = verbose_name


class 對齊狀態過濾器(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = '對齊狀態'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'tui3tse5'

    def lookups(self, request, model_admin):
        """
        (URL query, human-readable menu item)
        """
        return (
            ('alignissue', '校對錯誤'),
        )

    def queryset(self, request, queryset):
        # decide how to filter the queryset.
        if self.value() == 'alignissue':
            return queryset.filter(
                校對者__isnull=False
            ).exclude(對齊狀態__狀態__exact='')


class 校對表管理(ReadOnlyAdminFields, admin.ModelAdmin):
    # change list
    list_display = [
        'id', '語者', '音檔', '狀況',
        '漢字', '本調臺羅', '口語調臺羅',
        '備註開頭',
        '校對者', '校對時間',
        '對齊狀態'
    ]
    ordering = ['校對者', 'id', ]
    list_filter = ['語料狀況', '校對者', '音檔', 對齊狀態過濾器]
    search_fields = [
        '漢字', '本調臺羅', '口語調臺羅',
    ]
    list_per_page = 20

    # change view
    # venv/lib/python3.5/site-packages/django/contrib/admin/templates/admin/
    change_list_template = 'admin/gi2_liau7_khoo3/語料表/custom_change_list.html'
    change_form_template = 'admin/gi2_liau7_khoo3/語料表/custom_change_form.html'
    readonly_fields = ('音檔',)
    fieldsets = (
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
        models.TextField: {'widget': Textarea(
                           attrs={'rows': 2,
                                  'style': 'resize: none; min-width: 80%;'})},
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

    def save_model(self, request, obj, form, change):
        # 儲存校對者
        obj.校對者 = request.user
        super(校對表管理, self).save_model(request, obj, form, change)

    def has_add_permission(self, request):
        # 薛：只能由程式上傳音檔和語料
        # 薛：任何人都不能從後台新增
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_queryset(self, request):
        qs = super(校對表管理, self).get_queryset(request)
        return qs.filter(
            Q(愛先做無=True) |
            Q(sing5hong5有揀出來用無=True)
        )

    class Media:
        css = {
            "all": ("css/admin_gi2_liau7_pio2.css", "css/moedictFont.css")
        }
