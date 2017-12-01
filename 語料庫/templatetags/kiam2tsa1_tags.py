from django import template
from django.utils.datetime_safe import date
from 語料庫.管理.檢查 import 檢查表

register = template.Library()


@register.simple_tag
def 今仔日檢查數量():
    數量 = 檢查表.objects.filter(檢查時間__date=date.today()).count()
    return 數量


@register.simple_tag
def 賰檢查數量():
    數量 = (
        檢查表.objects
        .filter(校對者__isnull=False)
        .filter(檢查者__isnull=True)
        .count()
    )
    return 數量
