from django.db import models


class 語料狀況表(models.Model):
    狀況 = models.CharField(default='', max_length=30)

    def __str__(self):
        return self.狀況


class 音檔表(models.Model):
    類別 = models.CharField(
        max_length=20,
        choices=(
            ('戲劇', '戲劇'),
            ('朗讀', '朗讀'),
            ('新聞', '新聞'),
            ('對話', '對話'),
        ),
    )
    原始檔 = models.FileField(blank=True)
    資料夾名=models.CharField(max_length=50)
    聲音檔名=models.CharField(max_length=200)
    聽拍檔名=models.CharField(max_length=200)
    加入時間 = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.原始檔.name


class 語料表(models.Model):
    音檔 = models.ForeignKey(
        音檔表, related_name='資料',
        on_delete=models.CASCADE, null=True
    )
    聲音開始時間 = models.FloatField()
    聲音結束時間 = models.FloatField()

    漢字 = models.TextField(blank=True)
    書寫 = models.TextField(blank=True)
    斷詞 = models.TextField(blank=True)
    音值 = models.TextField(blank=True)
    華語 = models.TextField(blank=True)

    頭一版資料 = models.TextField(blank=True)
    sing5hong5認為會使 = models.BooleanField(default=False)
    ricer認為會使 = models.BooleanField(default=False)

    語料狀況 = models.ManyToManyField(語料狀況表)

    def 類別(self):
        return self.音檔.類別

    def 對齊狀態(self):
        '改去cache表'
        return True
