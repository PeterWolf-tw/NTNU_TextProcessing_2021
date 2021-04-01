#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json
import re

#讀取 json 的程式
def jsonTextReader(jsonFilePath):
    with open(jsonFilePath, encoding = 'utf-8') as f :
        content = f.read()
    content = json.loads(content)
    return content["text"]

#將字串轉為「句子」列表的程式
def text2Sentence(inputSTR):
    for i in range (len(inputSTR)):
        if inputSTR[i] == ",":
            if re.match( r"[0-9],[0-9]", inputSTR[i-1:i+2]):
                pass
            else :
                inputSTR = inputSTR[:i]+"<MyCuttingMark>"+inputSTR[i+1:]
    for i in ("...","…"):
        inputSTR = inputSTR.replace(i,"")
    for i in ( "、", "，", "。"):
        inputSTR = inputSTR.replace(i,"<MyCuttingMark>")
    output_LIST = inputSTR.split("<MyCuttingMark>")
    return output_LIST[:-1]


if __name__== "__main__":
    #設定要讀取的 news.json 路徑
    path = "./example/news.json"
    #將 news.json 利用 [讀取 json] 的程式打開
    text = jsonTextReader(path)
    #將讀出來的內容字串傳給 [將字串轉為「句子」 列表」]的程式，存為 newsLIST
    news_LIST = text2Sentence(text)

    #設定要讀取的 test.json 路徑
    path = "./example/test.json" 
    #將 test.json 的 sentenceLIST 內容讀出，存為 testLIS
    with open(path, encoding = 'utf-8') as f :
        content = f.read()
    content = json.loads(content)
    test_LIST = content["sentence"]

    #測試是否達到作業需求
    if news_LIST == test_LIST:
        print("作業過關！")
    else:
        print("作業不過關，請回到上面修改或是貼文求助！")