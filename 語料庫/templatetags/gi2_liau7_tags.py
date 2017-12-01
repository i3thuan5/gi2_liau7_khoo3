from django import template
from django.db.models.query_utils import Q
from django.utils.datetime_safe import date
from 語料庫.管理.校對 import 校對表

register = template.Library()


@register.simple_tag
def 今仔日校對數量():
    數量 = 校對表.objects.filter(校對時間__date=date.today()).count()
    return 數量


@register.simple_tag
def 攏總校對數量():
    數量 = 校對表.objects.filter(校對者__isnull=False).count()
    return 數量


@register.simple_tag
def 賰校對數量():
    數量 = (
        校對表.objects
        .filter(Q(愛先做無=True) | Q(sing5hong5有揀出來用無=True))
        .filter(校對者__isnull=True)
        .count()
    )
    return 數量
