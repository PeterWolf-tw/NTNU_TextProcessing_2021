#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json, jieba, re, os

def text2cws(jsonFilePath):
    with open(jsonFilePath, encoding="utf-8") as f:#開啟.json格式的檔案
        jsonContent = f.read()                     #讀取檔案
    jsonContent = json.loads(jsonContent)          #載入內容
    jsonContent = jsonContent["BODY"]              #取得"BODY"欄位
    
    sentenceLIST = text2Sentence(jsonContent)      #先斷句
    resultLIST = []
    for s in sentenceLIST:
        resultLIST.append("|".join(jieba.cut(s)))  #再使用jieba斷詞
    return resultLIST

def text2Sentence(inputSTR):                       #斷句
    BlankMark = [" ", "...","…", "「", "」", "【", "】", "1、", "2、", "3、", "1.", "2.", "3.", "4."]
    CutMark = ["，", "。", "、", "？", "！", "：", "；", "（", "）", ":", ";", "-", "(",  ")", "／"]
    LastMark = ["<MyCuttingMark><MyCuttingMark><MyCuttingMark>", "<MyCuttingMark><MyCuttingMark>"]
    
    for i in BlankMark:
        inputSTR = inputSTR.replace(i, "")
        
    for j in range (len(inputSTR)):
        if inputSTR[j] == ",":
            if re.match( r"[0-9],[0-9]", inputSTR[j-1:j+2]):
                pass
            else:
                inputSTR = inputSTR[:j] + "<MyCuttingMark>" + inputSTR[j+1:]
                
    for k in CutMark:
        if "0800-" in inputSTR:
            inputSTR = inputSTR.replace("0800-", "<phone>")         
        if inputSTR.find(":00") != -1:
            inputSTR = inputSTR.replace(":00", "<time>")
        inputSTR = inputSTR.replace(k, "<MyCuttingMark>")
        
    for m in LastMark:
        inputSTR = inputSTR.replace(m, "<MyCuttingMark>")
        
    inputSTR = inputSTR.replace("<phone>", "0800-")         
    inputSTR = inputSTR.replace("<time>", ":00")         
    inputLIST = inputSTR.split("<MyCuttingMark>")
    return inputLIST[:-1]

def termFreq(inputLIST):
    result = {}
    for sentence in inputLIST:
        for word in sentence.split("|"):            
            if result.get(word):
                result[word] = result.get(word) + 1
            else:
                result[word] = 1 
    return result

def DealFolderFile(rootPath):                                    #處理資料夾中的檔案
    fileLIST = os.listdir(rootPath)                              #取得檔案列表
    #比較：os.walk遞迴指令是以方式搜尋檔案
    exampleLIST = []
    for file in fileLIST:
        exampleLIST.append("|".join(text2cws(rootPath+'/'+file)))#用"|"來分割每一個詞
    return termFreq(exampleLIST)

if __name__== "__main__":
    rootTUPLE = ("./example/health" , "./example/finance")
    print("#health")
    print(DealFolderFile(rootTUPLE[0]))
    print("#finance")
    print(DealFolderFile(rootTUPLE[1]))
    
    

#社群網站使用的文章格式不盡相同
#TermFrequency Inversed F(統計模型)
#POS(語言學結構)