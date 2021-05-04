#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
在week07_你的學號_分組隊名.py中，設計你的程式完成以下指定規格：
a.設計一 func() 名為 "text2cws(jsonFilePath)"，接受參數為一 .json 格式的檔案，
  並讀取 json 檔案中的"BODY" 欄位的字串，加以「斷句」以後，使用 Jieba 斷詞將每個
  句子進行斷詞處理，回傳值為一「斷詞處理後的列表」。
b.設計一 func() 名為 "termFreq(inputLIST)"，接受參數為列表，並依列表內容的「字串元素」
  建立一字典 dict 型別的變數，將每個字串元素視為 key，  整份文件中的，該字串元素出現的次數視為 value。
c.設計一程式進入點，透過前述 "text2cws()" 讀取 example/health/ 中所有檔案的 "BODY" 欄位的值，再透過 termFreq() 計算每個斷詞處理後的字串出現的次數。
d.同樣的步驟，再對 example/finance/ 中所有的檔案再處理一次。
'''
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