from django import template
from 語料庫.models import 語料表
from django.utils.datetime_safe import date

register = template.Library()


@register.simple_tag
def 今仔日校對數量():
    數量 = 語料表.objects.filter(校對時間__date=date.today()).count()
    return 數量


@register.simple_tag
def 攏總校對數量():
    數量 = 語料表.objects.filter(校對者__isnull=False).count()
    return 數量


@register.simple_tag
def 賰校對數量():
    數量 = 語料表.objects.filter(校對者__isnull=True, sing5hong5有揀出來用無=True).count()
    return 數量
