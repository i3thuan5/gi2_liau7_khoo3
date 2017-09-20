# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-19 02:45
from __future__ import unicode_literals

from csv import DictReader
import io
from urllib.request import urlopen


from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.基本物件.公用變數 import 標點符號
from 語言模型.models import 語言模型表


def 匯入教典例句():
    for 句物件 in 教典資料.全部資料():
        語言模型表.objects.get_or_create(分詞=句物件.轉音(臺灣閩南語羅馬字拼音).看分詞())


class 教典資料:
    例句 = 'https://raw.githubusercontent.com/g0v/moedict-data-twblg/master/uni/%E4%BE%8B%E5%8F%A5.csv'

    @classmethod
    def 全部資料(cls):
        yield from cls._例句()

    @classmethod
    def _例句(cls):
        with urlopen(cls.詞目總檔網址) as 檔:
            with io.StringIO(檔.read().decode()) as 資料:
                for row in DictReader(資料):
                    音讀 = row['例句標音'].strip()
                    漢字 = row['例句'].strip()
                    整理後漢字 = 文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 漢字)
                    整理後臺羅 = 文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 音讀)
                    try:
                        句物件 = (
                            拆文分析器
                            .對齊句物件(整理後漢字, 整理後臺羅)
                        )
                        if 句物件.篩出字物件()[-1].型 in 標點符號:
                            yield 句物件
                    except Exception as 錯誤:
                        print(錯誤)
