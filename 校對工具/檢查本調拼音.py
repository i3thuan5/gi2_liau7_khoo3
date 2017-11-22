# -*- coding: utf-8 -*-

from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 用字.models import 用字表


def 判斷本調拼音(漢字, 本調臺羅):
    print('判斷本調拼音')
    結果 = 檢查本調拼音(漢字, 本調臺羅)
    回傳字串 = ''
    if type(結果) is list:
        回傳字串 = ' '.join(結果)
    else:
        回傳字串 = 結果
    return 回傳字串


def 檢查本調拼音(漢字, 本調臺羅):
    try:
        本調 = 拆文分析器.對齊句物件(
            漢字,
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 本調臺羅)
        ).轉音(臺灣閩南語羅馬字拼音)
    except Exception as 錯誤:
        錯誤結果 = str(錯誤).split('！')[0]
    else:
        錯誤結果 = []
        for 詞物件 in 本調.網出詞物件():
            for 字物件 in 詞物件.篩出字物件():
                if not 用字表.有這个字無(字物件):
                    錯誤結果.append(字物件.看分詞())
    return 錯誤結果
