from django.core.management.base import BaseCommand
from 語料庫.models import 語料表


class Command(BaseCommand):

    def handle(self, *args, **參數):
        for 語料 in 語料表.objects.all():
            語料.save()
