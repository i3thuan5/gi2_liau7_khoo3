from django.apps import AppConfig

import 檢查工具.signals
from 檢查工具 import signals


class 檢查工具Config(AppConfig):
    name = '檢查工具'

    def ready(self):
        # registering signals
        signals
        檢查工具.signals
