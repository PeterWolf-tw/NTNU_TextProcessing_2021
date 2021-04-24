#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
import jieba
import os
import json
#
def text2cws(jsonFilePath):
	with open( jsonFilePath, encoding="utf-8") as f:
		jsonContent = f.read()
	jsonContent = json.loads(jsonContent)
	# 取得 json "BODY" 欄位
	jsonContent = jsonContent["BODY"]
	# 斷句
	SentencetList =sentence2 ( jsonContent)
	#print( SentencetList)
	resultLIST = []
	for s in SentencetList:
		resultLIST.append("/".join(jieba.cut(s)))
	return resultLIST
    
#將字串轉為「句子」列表的程式
def sentence2(inputSTR):
    for item in ( "、", "，","。", ","):
        inputSTR = inputSTR.replace(item, "<MyCuttingMark>")
        
    inputSTR = inputSTR.replace("…", "")
    inputSTR = inputSTR.replace("...", "")
    if "2<MyCuttingMark>718" in inputSTR:
        inputSTR = inputSTR.replace("2<MyCuttingMark>718", "2,718")
    #inputSTR = inputSTR.strip("<MyCuttingMark>")#適用於字串，以清除結尾不要的東西
    resultLIST = inputSTR.split("<MyCuttingMark>")
    #return resultLIST
    return resultLIST[:-1]#作用同上，從後面扣回去。
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
if __name__== "__main__":
    
    # health
    healthDic = dealJsonInFile( "./python//example/health/")
    print( "health:", healthDic)

	# finance 	
    financeDic = dealJsonInFile( "./python//example/finance/")
    print( "finance:", financeDic)
