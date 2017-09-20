from django.core.management.base import BaseCommand
from 臺灣言語工具.語言模型.安裝KenLM訓練程式 import 安裝KenLM訓練程式
from 語言模型.models import 語言模型表


class Command(BaseCommand):

    def handle(self, *args, **參數):
        安裝KenLM訓練程式.安裝kenlm()
        語言模型表.訓練模型()
