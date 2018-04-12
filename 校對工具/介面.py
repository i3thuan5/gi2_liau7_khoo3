# -*- coding: utf-8 -*-
import Pyro4
from django.http.response import JsonResponse


try:
    _工具 = Pyro4.Proxy("PYRONAME:校對工具")
except Exception as 錯誤:
    print(錯誤)


def 標本調(request, 漢字, 臺羅):
    return JsonResponse({'本調': _工具.標本調(漢字, 臺羅)})


def 口語標漢字本調(request, 口語):
    漢字, 本調, _無處理輕聲的本調 = _工具.口語標漢字本調(口語)
    return JsonResponse({
        '漢字': 漢字,
        '本調': 本調,
    })
