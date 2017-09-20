from django.apps import AppConfig
from 臺灣言語工具.語言模型.安裝KenLM訓練程式 import 安裝KenLM訓練程式


class 校對工具Config(AppConfig):
    name = '校對工具'

    def ready(self):
        安裝KenLM訓練程式.安裝kenlm(編譯CPU數=2)