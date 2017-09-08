from django import template
from 語料庫.models import 語料表

register = template.Library()


@register.simple_tag
def 今仔日校對數量():
    數量 = 語料表.objects.get(pk=1).count()
    return 數量 