#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json
import re
import jieba
import os

#讀取 json "BODY" 欄位的字串，斷句後用 Jieba 斷詞處理後，回傳處理後的列表
def text2cws(jsonFilePath):
	with open( jsonFilePath, encoding="utf-8") as f:
		jsonContent = f.read()
	jsonContent = json.loads(jsonContent)
	# 取得 json "BODY" 欄位
	jsonContent = jsonContent["BODY"]
	# 斷句
	SentencetList = text2Sentence( jsonContent)
	# print( SentencetList)
	resultLIST = []
	for s in SentencetList:
		resultLIST.append("/".join(jieba.cut(s)))
	return resultLIST
#將字串轉為「句子」列表的程式
def text2Sentence(inputSTR):
	for i in ("...", "…"):
		inputSTR = inputSTR.replace( i, "")
	for i in range(len(inputSTR)):
		if inputSTR[i] == ",":
			if  re.match( r"[0-9],[0-9]", inputSTR[i-1:i+2]):
				inputSTR = inputSTR[0:i] + ' ' + inputSTR[i+1:] 
	for i in ( "、", "，", "。", ",",";","；"):
		inputSTR = inputSTR.replace( i, "<MyCuttingMark@CSIE112_Grammyship>")
	for i in range(len(inputSTR)):
		if inputSTR[i] == " ":
			if re.match( r"[0-9] [0-9]", inputSTR[i-1:i+2]):
				inputSTR = inputSTR[0:i] + ',' + inputSTR[i+1:]
	inputLIST = inputSTR.split("<MyCuttingMark@CSIE112_Grammyship>")
	return inputLIST[:-1]
# 字串元素出現次數 Dict
def termFreq(inputLIST):
	dic = dict() 
	for s in inputLIST:
		for word in s.split("/"):
			if dic.get(word) :
				dic[word] = dic.get(word)+1
			else:
				dic[word] = 1
	return dic

# 讀取 json，text2cwt() 讀取"BODY"欄位後斷句，termFreq() 計算斷詞處理後的元素次數
def dealJsonInFile(folderPath):
	# 讀取資料夾中所有 json 
	jiebaList = []
	for f in os.listdir( folderPath):
		# check is json file 
		if f.endswith(".json"):
			jiebaList.extend(text2cws(os.path.join( folderPath, f))) 
	# print( jiebaList)
	resultDic = termFreq( jiebaList )
	return resultDic


if __name__== "__main__":
    
    # health
    healthDic = dealJsonInFile( "./example/health/")
    print( "health:", healthDic)

	# finance 	
    financeDic = dealJsonInFile( "./example/finance/")
    print( "finance:", financeDic)
    