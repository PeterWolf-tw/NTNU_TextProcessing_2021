#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
在week07_你的學號_分組隊名.py中，設計你的程式完成以下指定規格：
a.設計一 func() 名為 "text2cws(jsonFilePath)"，接受參數為一 .json 格式的檔案，
  並讀取 json 檔案中的"BODY" 欄位的字串，加以「斷句」以後，使用 Jieba 斷詞將每個
  句子進行斷詞處理，回傳值為一「斷詞處理後的列表」。
b.設計一 func() 名為 "termFreq(inputLIST)"，接受參數為列表，並依列表內容的「字串元素」
  建立一字典 dict 型別的變數，將每個字串元素視為 key，  整份文件中的，該字串元素出現的次數視為 value。
c.設計一程式進入點，透過前述 "text2cws()" 讀取 example/health/ 中所有檔案的 "BODY" 欄位的值，再透過 termFreq() 計算每個斷詞處理後的字串出現的次數。
d.同樣的步驟，再對 example/finance/ 中所有的檔案再處理一次。
'''
import os
import errno
import json
import jieba


def text2cws(path):
    with open(path, encoding="utf-8")as f:
        js = f.read()
    js = json.loads(js)
    STR = js["BODY"]
    STR.replace(" ", "")
    for item in ("「", "，", "、", "」", "。", "\"", ","):
        STR = STR.replace(item, "<mark>")
    STRLIST = STR.split("<mark>")
    # print(STRLIST)
    returnLIST = []
    for item in STRLIST:
        returnLIST.append('/'.join(jieba.cut(item)))

    return returnLIST


def termFreq(inputLIST):
    r = {}
    for sen in inputLIST:
        for word in sen.split("/"):
            if word not in r:
                r[word] = 1
            else:
                r[word] += 1
    return r


def topFreq(dict):
    top = 0
    topname = ""
    for word in dict:
        if dict[word] > top:
            top = dict[word]
            topname = word
    print(topname, " : ", top)


def main():
    rootPath = "example/health/"
    words = []
    for file in os.listdir(rootPath):
        if file.endswith(".json"):
            words += text2cws(rootPath + file)
        else:
            continue

    top = termFreq(words)
    print(top)
    rootPath = "example/finance/"
    words = []
    for file in os.listdir(rootPath):
        if file.endswith(".json"):
            words += text2cws(rootPath + file)
        else:
            continue
    print("\n\n\n\n")
    print(termFreq(words))
    top = termFreq(words)
    print(top)


if __name__ == "__main__":
    main()
