#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json
import re
import jieba
import os


def text2cws(jsonFilePath):
	with open( jsonFilePath, encoding="utf-8") as f:
		jsonContent = f.read()
	jsonContent = json.loads(jsonContent)
	jsonContent = jsonContent["BODY"]
	SentencetList = text2Sentence( jsonContent)
	resultLIST = []
	for s in SentencetList:
		resultLIST.append("/".join(jieba.cut(s)))
	return resultLIST

def text2Sentence(inputSTR):
	for i in ("...", "…"):
		inputSTR = inputSTR.replace( i, "")
	for i in range(len(inputSTR)):
		if inputSTR[i] == ",":
			if  re.match( r"[0-9],[0-9]", inputSTR[i-1:i+2]):
				inputSTR = inputSTR[0:i] + ' ' + inputSTR[i+1:] 
	for i in ( "、", "，", "。", ",",";","；"):
		inputSTR = inputSTR.replace( i, "<MyCuttingMark@CSIE112_Sophie8909>")
	for i in range(len(inputSTR)):
		if inputSTR[i] == " ":
			if re.match( r"[0-9] [0-9]", inputSTR[i-1:i+2]):
				inputSTR = inputSTR[0:i] + ',' + inputSTR[i+1:]
	inputLIST = inputSTR.split("<MyCuttingMark@CSIE112_Sophie8909>")
	return inputLIST[:-1]

def termFreq(inputLIST):
	dic = dict() 
	for s in inputLIST:
		for word in s.split("/"):
			if dic.get(word) :
				dic[word] = dic.get(word)+1
			else:
				dic[word] = 1
	return dic


def dealJsonInFile(folderPath):
	jiebaList = []
	for f in os.listdir( folderPath):
		if f.endswith(".json"):
			jiebaList.extend(text2cws(os.path.join( folderPath, f))) 
	resultDic = termFreq( jiebaList )
	return resultDic


if __name__== "__main__":
    healthDic = dealJsonInFile( "./example/health/")
    print( "health:", healthDic)
    financeDic = dealJsonInFile( "./example/finance/")
    print( "finance:", financeDic)