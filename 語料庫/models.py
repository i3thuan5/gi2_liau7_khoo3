from os.path import join

from django.conf import settings
from django.db import models
from 臺灣言語工具.語音辨識.聲音檔 import 聲音檔
from django.contrib.auth.models import User


class 音檔表(models.Model):
    類別 = models.CharField(
        max_length=20,
        choices=(
            ('戲劇', '戲劇'),
            ('朗讀', '朗讀'),
            ('新聞', '新聞'),
            ('對話', '對話'),
        ),
        db_index=True,
    )
    原始檔 = models.FileField(blank=True)
    資料夾名 = models.CharField(max_length=50)
    聲音檔名 = models.CharField(max_length=200)
    聽拍檔名 = models.CharField(max_length=200)
    加入時間 = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        unique_together = (("資料夾名", "聽拍檔名"),)
        ordering = ['資料夾名', '聲音檔名', '聽拍檔名']

    def __str__(self):
        return self.原始檔.name

    def 聲音檔(self):
        return 聲音檔.對檔案讀(join(settings.MEDIA_ROOT, self.原始檔.name))


class 語料表(models.Model):
    音檔 = models.ForeignKey(
        音檔表, related_name='資料',
        on_delete=models.CASCADE
    )
    聲音開始時間 = models.FloatField()
    聲音結束時間 = models.FloatField()
    語者 = models.CharField(max_length=50, db_index=True)

    # Edit
    漢字 = models.TextField(blank=True)
    本調臺羅 = models.TextField(blank=True)
    口語調臺羅 = models.TextField(blank=True)
    華語 = models.TextField(blank=True)
    語料狀況 = models.ManyToManyField('語料狀況表', blank=True)
    校對者 = models.ForeignKey(User, null=True)
    校對時間 = models.DateTimeField(null=True)
    備註 = models.TextField(blank=True)

    # Original data backup
    頭一版資料 = models.TextField(blank=True)
    頭一版通用 = models.TextField(blank=True)

    # Tags for Kaldi
    sing5hong5舊編號 = models.CharField(null=True, max_length=200)
    sing5hong5新編號 = models.CharField(null=True, max_length=200)
    sing5hong5有揀出來用無 = models.BooleanField(default=False)

    class Meta:
        verbose_name = "語料表"
        verbose_name_plural = verbose_name

    def 類別(self):
        return self.音檔.類別

    def 對齊狀態(self):
        '改去cache表'
        return True

    def __str__(self):
        return '{} {}'.format(self.id, self.漢字)


class 語料狀況表(models.Model):
    狀況 = models.CharField(unique=True, max_length=30)

    class Meta:
        verbose_name = "狀況表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{} {}'.format(self.pk, self.狀況.split('：')[-1])
