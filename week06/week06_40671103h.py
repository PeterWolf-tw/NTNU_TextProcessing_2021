#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json

def jsonTextReader(jsonFilePath):#讀取 json 的程式
    with open(jsonFilePath, encoding="utf-8") as f:#將讀入的json檔案以純文字載入並回傳
        text = json.loads(f.read())
    return text



def text2Sentence(inputSTR):#將字串轉為「句子」列表的程式

    symbol=[ "、", "，","。", ","] #斷句符號
    for i in symbol :
        inputSTR = inputSTR.replace(i,"|")
    inputSTR = inputSTR.replace("…", "")
    inputSTR = inputSTR.replace("...", "")

    if "|" in inputSTR:
        inputSTR = inputSTR.replace("2|718", "2,718")

    sentenceLIST = inputSTR.split("|")
    return sentenceLIST[:len(sentenceLIST)-1]

if __name__== "__main__":
    news_loc = "./example/news.json" #設定要讀取的 news.json 路徑

    news_text = jsonTextReader(news_loc)#將 news.json 利用 [讀取 json] 的程式打開

    news_LIST = text2Sentence(news_text['text']) #將讀出來的內容字串傳給 [將字串轉為「句子」 列表」]的程式，存為 newsLIST

    test_loc = "./example/test.json"#設定要讀取的 test.json 路徑

    test_LIST = jsonTextReader(test_loc)['sentence']#將 test.json 的 sentenceLIST 內容讀出，存為 testLIS

    #測試是否達到作業需求
    if news_LIST == test_LIST:
        print("作業過關！")
    else:
        print("作業不過關，請回到上面修改或是貼文求助！")