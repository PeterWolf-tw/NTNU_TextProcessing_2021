#!/usr/bin/env python3
# -*- coding:utf-8 -*-


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
    returnLIST = []
    for item in STRLIST:
        returnLIST.append('/'.join(jieba.cut(item)))

    return returnLIST

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