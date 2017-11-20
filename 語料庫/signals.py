from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from 校對工具.檢查本調拼音 import 判斷本調拼音

@receiver(post_save, sender='語料庫.語料表')
def 新增對齊狀態(sender, instance, **kwargs):
    """create 對齊狀態 for every new 語料."""
    print("""create 對齊狀態 for every new 語料.""")
    print('instance=', instance)
#     if getattr(instance, '漢字', True) and getattr(instance, '本調臺羅', True):
#         狀態字串 = 判斷本調拼音(instance.漢字, instance.本調臺羅)
#         if created:
#             新狀態 = 對齊狀態表(狀態=狀態字串)
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
