#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json
import re

#讀取 json 的程式
def jsonTextReader(jsonFilePath):
	with open( jsonFilePath, encoding="utf-8") as f:
		jsonContent = f.read()
	jsonContent = json.loads(jsonContent)
	try:
		return jsonContent["text"]
	except:
		return jsonContent["sentence"]
#將字串轉為「句子」列表的程式
def text2Sentence(inputSTR):
	for i in ("...", "…"):
		inputSTR = inputSTR.replace( i, "")
	for i in range(len(inputSTR)):
		if inputSTR[i] == ",":
			if  re.match( r"[0-9],[0-9]", inputSTR[i-1:i+2]):
				inputSTR = inputSTR[0:i] + ' ' + inputSTR[i+1:] 
	for i in ( "、", "，", "。", ","):
		inputSTR = inputSTR.replace( i, "<MyCuttingMark>")
	for i in range(len(inputSTR)):
		if inputSTR[i] == " ":
			if re.match( r"[0-9] [0-9]", inputSTR[i-1:i+2]):
				inputSTR = inputSTR[0:i] + ',' + inputSTR[i+1:]
	inputLIST = inputSTR.split("<MyCuttingMark>")
	return inputLIST[:-1]

if __name__== "__main__":
    #設定要讀取的 news.json 路徑
    newsjsonPath = "./example/news.json"
    #將 news.json 利用 [讀取 json] 的程式打開
    newsSTR = jsonTextReader( newsjsonPath)
    #將讀出來的內容字串傳給 [將字串轉為「句子」 列表」]的程式，存為 newsLIST
    news_LIST = text2Sentence( newsSTR )
    # print( news_LIST)
    #設定要讀取的 test.json 路徑
    testjsonPath = "./example/test.json"
    #將 test.json 的 sentenceLIST 內容讀出，存為 testLIST
    test_LIST = jsonTextReader( testjsonPath )
    # print( test_LIST)
    #測試是否達到作業需求
    if news_LIST == test_LIST:
        print("作業過關！")
    else:
        print("作業不過關，請回到上面修改或是貼文求助！")