from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from 校對工具.檢查本調拼音 import 判斷本調拼音
from 語料庫.models import 對齊狀態表

@receiver(post_save, sender='語料庫.語料表')
def 新增對齊狀態(sender, instance, **kwargs):
    print('新增對齊狀態')
    """create 對齊狀態 for every new 語料."""
    if getattr(instance, '漢字', True) and getattr(instance, '本調臺羅', True):
        狀態字串 = 判斷本調拼音(instance.漢字, instance.本調臺羅)
#         print('instance=', instance.__dict__)
        try:
            print('old state=', instance.對齊狀態.狀態)
            原始狀態 = instance.對齊狀態
            原始狀態.狀態 = 狀態字串
            print('狀態字串=', 狀態字串)
            原始狀態.save()
            print('new state=', instance.對齊狀態.狀態)
            
        except 對齊狀態表.DoesNotExist:
            print('except')
            #新增狀態
            新對齊狀態 = 對齊狀態表(語料=instance, 狀態=狀態字串)
            新對齊狀態.save()