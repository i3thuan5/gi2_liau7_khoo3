from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import transaction
from 語言模型.models import 語言模型表
from 口語辭典.models import 口語辭典表
from 本調辭典.models import 本調辭典表


class Command(BaseCommand):

    def handle(self, *args, **參數):
        with transaction.atomic():
            本調辭典表.objects.all().delete()
            call_command('教典匯入本調辭典')
            口語辭典表.objects.all().delete()
            call_command('本調辭典轉口語辭典')
            call_command('校對語句匯口語辭典')
            語言模型表.objects.all().delete()
            call_command('匯入教典例句')
            call_command('匯入校對語句')            
            call_command('訓練語言模型')
