# 語料庫整理
[![Build Status](https://travis-ci.org/i3thuan5/gi2_liau7_khoo3.svg?branch=master)](https://travis-ci.org/i3thuan5/gi2_liau7_khoo3)
[![Coverage Status](https://coveralls.io/repos/github/i3thuan5/gi2_liau7_khoo3/badge.svg?branch=master)](https://coveralls.io/github/i3thuan5/gi2_liau7_khoo3?branch=master)

## 安裝
```
sudo apt-get install normalize-audio
virtualenv --python=python3 venv; . venv/bin/activate; pip install --upgrade pip # 設置環境檔
pip install django Taiwanese-Speech-And-Text-Corpus
```

## 匯入資料
```
time python manage.py 匯入1_0版語料 ../Ko_corpus/TL-Json ~/Dropbox/母語/語料/高老師聽拍語料/Finished/ MH MaternalHome-003\|25\|110308\|MaternalHome-003-101223.json
```