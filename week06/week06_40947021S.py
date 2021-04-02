#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
# 讀取 json 的程式


def jsonTextReader(path):
    with open(path, encoding="utf-8")as f:
        txt = f.read()
    txt = json.loads(txt)
    try:
        return txt["text"]
    except:
        return txt["sentence"]

# 將字串轉為「句子」列表的程式


def text2Sentence(inputSTR):
    inputSTR = inputSTR.replace("…", "")
    inputSTR = inputSTR.replace("...", "")
    for item in ("「", "，", "、", "」", "。", "\"", ","):
        inputSTR = inputSTR.replace(item, "<mark>")
    while "2<mark>718" in inputSTR:
        inputSTR = inputSTR.replace("2<mark>718", "2,718")

    inputSTR = inputSTR.split("<mark>")

    return inputSTR


if __name__ == "__main__":
    # 設定要讀取的 news.json 路徑
    jsonPath = "./example/news.json"
    # 將 news.json 利用 [讀取 json] 的程式打開
    newsFile = jsonTextReader(jsonPath)
    # 將讀出來的內容字串傳給 [將字串轉為「句子」 列表」]的程式，存為 newsLIST
    news_LIST = text2Sentence(newsFile)
    news_LIST.pop(len(news_LIST)-1)
    # 設定要讀取的 test.json 路徑
    testPath = "./example/test.json"
    # 將 test.json 的 sentenceLIST 內容讀出，存為 testLIS
    testFile = jsonTextReader(testPath)
    test_LIST = testFile
    # 測試是否達到作業需求
    if news_LIST == test_LIST:
        print("作業過關！")
    else:
        print("作業不過關，請回到上面修改或是貼文求助！")