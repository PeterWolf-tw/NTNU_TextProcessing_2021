#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
from ArticutAPI import ArticutAPI
from pprint import pprint
from requests import post

'''
CODE BY CSIE112
'''

# 把 week11.py 改名為  week11_分組隊名.py 放入你的隊名目錄中
# 在 week11_分組隊名.py 中，設計你的程式，利用 Jieba/CKIPTagger/Articut 任選一種 NLP 工具完成以下指定規格：
# 把 "dbp.txt" 和 "pbd.txt" 的內容取出進行詞頻計算。

# 計算兩文本的「字符」出現次數 (如同本簡報 p8 上半頁)，並存成 charCount_dbp 和 charCount_pbd


# 計算兩文本的「字詞」出現次數 (如同本簡報 p8 下半頁)，並存成 wordCount_dbp 和 wordChount_pbd


# 計算兩文本含有詞性標記的字詞出現次數 (如本簡報 p9)，並存成 posWordCount_dbp 和 posWordCount_pbd


# 計算兩文本「去除功能詞」(如本簡報 p10)，並存成 contentWord_dbp 和 contentWord_pbd 


# 將以上所有的 _dbp 都存入 count_result.json 裡


# 請仔細觀察前述兩兩一組的 _dbp vs. _pbd 的結果，並小組討論「是否能從詞頻裡分辨究竟哪一篇是人咬狗，哪一篇是狗咬人？。若能，是為什麼，若不能，又是為什麼。」討論結果請另存成 discussion_分隊隊名.txt 一併上傳到課程 week11 的 repo 裡。


if __name__== "__main__":
