#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#讀取 json 的程式
import json 
def jsonReader(jsonFILE):
    with open(jsonFILE, encoding="utf-8") as f:
        txtDICT = json.load(f.read())
    return txtDICT

#將字串轉為「句子」列表的程式
def sentence2LIST_v1(inputSTR):
    for item in ("「", "，", "_", "」", "。"):
        inputSTR = inputSTR.replace(item, item + "<MyCuttingMark>")#在". "或", "item的後面加上標記
    resultLIST = inputSTR.split("<MyCuttingMark>")
    return resultLIST

if __name__== "__main__":
    #設定要讀取的 news.json 路徑
    jsonFILE = "./example/news.json"
    #將 news.json 利用 [讀取 json] 的程式打開
    jsonDICT = jsonReader(jsonFILE)
    #將讀出來的內容字串傳給 [將字串轉為「句子」 列表」]的程式，存為 newsLIST
    news_LIST = sentence2LIST_v1(jsonDICT["text"])
    #設定要讀取的 test.json 路徑
    textJsonFILE = "./example/news.json"
    #將 test.json 的 sentenceLIST 內容讀出，存為 testLIS
    textJsonDICT = jsonReader(textJsonFILE)
    text_LIST = sentence2LIST_v1(textJsonFILE["text"]) 

    #測試是否達到作業需求
    if news_LIST == test_LIST:
        print("作業過關！")
    else:
        print("作業不過關，請回到上面修改或是貼文求助！")