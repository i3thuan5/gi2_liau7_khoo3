from django.apps import AppConfig


class 檢查工具Config(AppConfig):
    name = '檢查工具'

    def ready(self):
        # registering signals
        from 檢查工具 import signals
        signals
