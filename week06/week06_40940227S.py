#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json

#讀取 json 的程式
def jsonTextread(path, target):
    with open(path,encoding="utf-8") as f:
        inputtext = json.load(f)[target]
    return inputtext

#將字串轉為「句子」列表的程式
def text2Sentence(inputSTR):
    sentence_LIST = []
    start = 0
    k = 0
    length_STR = len(inputSTR)
    while k < length_STR:
        for i in [".","…"]:
            while inputSTR[k]==i:
                inputSTR=inputSTR[:k]+inputSTR[k+1:]
                length_STR=len(inputSTR)
        k = k+1
    for i in range(0,length_STR):
        number = 0
        if (inputSTR[i]==","):
            for j in range(0,10):
                if((inputSTR[i-1]==str(j))|(inputSTR[i+1]==str(j))):
                    number = number+1
                    print("ya")
            if (number == 2):
                pass
                print("NO!")
            else:
                sentence_LIST.append(inputSTR[start:i])
                start = i+1
                print("Ya")
        for j in ["、","，","。"]:
            if (inputSTR[i]==j):
                sentence_LIST.append(inputSTR[start:i])
                start = i+1
                break

    return sentence_LIST
        
if __name__== "__main__":
    #設定要讀取的 news.json 路徑
    path_STR = "./example/news.json"
    #將 news.json 利用 [讀取 json] 的程式打開
    inputSTR = jsonTextread(path_STR,"text")
    #將讀出來的內容字串傳給 [將字串轉為「句子」 列表」]的程式，存為 newsLIST
    news_LIST = text2Sentence(inputSTR)
    #設定要讀取的 test.json 路徑
    path_TEXT = "./example/test.json"
    #將 test.json 的 sentenceLIST 內容讀出，存為 testLIST
    test_LIST = jsonTextread(path_TEXT,"sentence")
    #測試是否達到作業需求
    print(news_LIST)
    print(test_LIST)
    if news_LIST == test_LIST:
        print("作業過關！")
    else:
        print("作業不過關，請回到上面修改或是貼文求助！")
