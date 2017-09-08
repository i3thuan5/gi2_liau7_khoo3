from django import template
from 語料庫.models import 語料表
from django.utils.datetime_safe import date

register = template.Library()


@register.simple_tag
def 今仔日校對數量():
    數量 = 語料表.objects.filter(校對時間__date=date.today()).count()
    return 數量 