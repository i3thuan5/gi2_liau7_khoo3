import re


class 文本分析:
    代號 = 'X'
    _代換 = re.compile('（[^）]+）')

    @classmethod
    def 漢字合音轉做代號(cls, 漢字):
        return cls._代換.sub(' ' + cls.代號 + ' ', 漢字)

    @classmethod
    def 這字的漢字敢是合音(cls, 字物件):
        return 字物件.型 == cls.代號
