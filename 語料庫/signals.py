from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from 校對工具.檢查本調拼音 import 判斷本調拼音
from 語料庫.models import 對齊狀態表
from 語料庫.models import 語料表

@receiver(post_save, sender='語料庫.語料表')
def 新增對齊狀態(sender, instance, **kwargs):
    """create 對齊狀態 for every new 語料."""
    print('instance=', instance)
    print('length 語料表',語料表.objects.all().count())
    print('length 對齊狀態表',對齊狀態表.objects.all().count())
    if getattr(instance, '漢字', True) and getattr(instance, '本調臺羅', True):
        狀態字串 = 判斷本調拼音(instance.漢字, instance.本調臺羅)
        print('pk=', instance.pk)
        原始狀態 = instance.對齊狀態
        print('原始狀態=', 原始狀態)
        if 原始狀態:
            原始狀態.狀態 = 狀態字串
            原始狀態.save()
        else:
            新對齊狀態 = 對齊狀態表(狀態=狀態字串)
            新對齊狀態.save()
            語料表.objects.filter(pk=instance.pk).update(對齊狀態=新對齊狀態) 
        print('length 對齊狀態表 new',對齊狀態表.objects.all().count())
        print('new instance=', instance.__dict__)

#         else:
#             
# #             
# #             try:
# #                 self.對齊狀態.狀態 = 狀態字串
# #             except AttributeError:
# #                 print('新增, 狀態字串=', 狀態字串)
# #                 新狀態 = 對齊狀態表(狀態=狀態字串)
# #                 self.對齊狀態 = 新狀態
# #             self.對齊狀態.save()
#             對齊狀態表.objects.create(thing=instance)
