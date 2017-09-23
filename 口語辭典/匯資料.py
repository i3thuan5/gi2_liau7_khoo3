# -*- coding: utf-8 -*-

from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 口語辭典.models import 口語辭典表
from 校對工具.models import 辭典表
from 程式.全漢全羅.做辭典 import 可能的變調
from 臺灣言語工具.基本物件.公用變數 import 標點符號


def 轉到口語辭典():
    for 詞物件 in _全部資料():
        if 詞物件.篩出字物件()[0].音 not in 標點符號:
            口語辭典表.匯詞物件(詞物件.轉音(臺灣閩南語羅馬字拼音))


def _全部資料():
    for 分詞 in 辭典表.全部分詞():
        yield from 可能的變調(拆文分析器.分詞詞物件(分詞))
