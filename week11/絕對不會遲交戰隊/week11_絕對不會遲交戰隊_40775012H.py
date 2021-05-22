#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
from ArticutAPI import ArticutAPI

def jsonTextReader(jsonFilePath):
    with open(jsonFilePath,  encoding = "utf-8") as f:
        Content = f.read()
    return Content    

def jsonFileWriter(jsonDICT, jsonFileName):
    with open(jsonFileName, mode="w") as f:
        json.dump(jsonDICT, f, ensure_ascii=False)
    return None

def charCounter(inputSTR):#計算「字符」出現次數
    charDICT = {}
    for i in inputSTR:
        if i in charDICT:
            pass
        else:
            charDICT[i] = inputSTR.count(i)
    charCountLIST = []
    for i in charDICT.items():
        charCountLIST.append(i)
    charCountLIST.sort(key=lambda c: c[1], reverse=True)
    return charCountLIST

def wordCounter(inputSTR):#計算「字詞」出現次數
    inputLIST = inputSTR.split("/")
    wordDICT = {}
    for w in inputLIST:
        if w in wordDICT:
            pass
        else:
            wordDICT[w] = inputLIST.count(w)
    wordCountLIST = []
    for i in wordDICT.items():
        wordCountLIST.append(i)
    wordCountLIST.sort(key=lambda c: c[1], reverse=True)
    return wordCountLIST

def wordPlusPosCounter(inputSTR):#計算「字詞 + 詞性」出現次數
    inputSTR = inputSTR.replace("><", ">MY_SPLITTER<")
    inputLIST = inputSTR.split("MY_SPLITTER")
    wordDICT = {}
    for w in inputLIST:
        if w in wordDICT:
            pass
        else:
            wordDICT[w] = inputLIST.count(w)
    wordCountLIST = []
    for i in wordDICT.items():
        wordCountLIST.append(i)

    wordCountLIST.sort(key=lambda c: c[1], reverse=True)
    return wordCountLIST

def contentWordPlusPosCounter(inputSTR):#計算「內容字詞」(非功能字/詞)出現次數
    inputLIST = inputSTR.split("/")
    wordDICT = {}
    for w in inputLIST:
        if w in wordDICT:
            pass
        else:
            wordDICT[w] = inputLIST.count(w)
    wordCountLIST = []
    for i in wordDICT.items():
        wordCountLIST.append(i)
    wordCountLIST.sort(key=lambda c: c[1], reverse=True)
    return wordCountLIST


if __name__== "__main__":
    #把 "dbp.txt" 和 "pbd.txt" 的內容取出進行詞頻計算。
    fileTUPLE = ("../example/dbp.txt", "../example/pbd.txt")
    dbpSTR = jsonTextReader(fileTUPLE[0])
    
    pbdSTR = jsonTextReader(fileTUPLE[1])   
    #計算兩文本的「字符」出現次數 (如同本簡報 p8 上半頁)，並存成 charCount_dbp 和 charCount_pbd
    charCount_dbp = charCounter(dbpSTR)
    print(charCount_dbp)
    
    charCount_pbd = charCounter(pbdSTR)
    print(charCount_pbd)
    #計算兩文本的「字詞」出現次數 (如同本簡報 p8 下半頁)，並存成 wordCount_dbp 和 wordChount_pbd
    articut = ArticutAPI.Articut()
    segdbpSTR = ""
    for i in range(0, len(dbpSTR), 2000):
        dbpDICT = articut.parse(dbpSTR[i:i+2000])
        segdbpSTR = segdbpSTR + dbpDICT["result_segmentation"]
    print(segdbpSTR)
    wordCount_dbp = wordCounter(segdbpSTR)
    print(wordCount_dbp)
    
    segpbdSTR = ""
    for i in range(0, len(pbdSTR), 2000):
        pbdDICT = articut.parse(pbdSTR[i:i+2000])
        segpbdSTR = segpbdSTR + pbdDICT["result_segmentation"]
    print(segpbdSTR)
    wordCount_pbd = wordCounter(segpbdSTR)
    print(wordCount_pbd)    
    #計算兩文本含有詞性標記的字詞出現次數 (如本簡報 p9)，並存成 posWordCount_dbp 和 posWordCount_pbd
    posdbpLIST = []
    for i in range(0, len(dbpSTR), 2000):
        dbpDICT = articut.parse(dbpSTR[i:i+2000])
        posdbpLIST.extend(dbpDICT["result_pos"])
    posdbpSTR = "".join([p for p in posdbpLIST if len(p) > 1])
    posWordCount_dbp = wordPlusPosCounter(posdbpSTR)
    print(posWordCount_dbp)

    pospbdLIST = []
    for i in range(0, len(pbdSTR), 2000):
        pbdDICT = articut.parse(pbdSTR[i:i+2000])
        pospbdLIST.extend(pbdDICT["result_pos"])
    pospbdSTR = "".join([p for p in pospbdLIST if len(p) > 1])
    posWordCount_pbd = wordPlusPosCounter(pospbdSTR)
    print(posWordCount_pbd)
    #計算兩文本「去除功能詞」(如本簡報 p10)，並存成 contentWord_dbp 和 contentWord_pbd 
    contentdbpLIST = []
    for i in range(0, len(dbpSTR), 2000):
        resultDICT = articut.parse(dbpSTR[i:i+2000])
        contentdbpLIST = articut.getContentWordLIST(dbpDICT)
        for c in contentdbpLIST:
            if len(c) > 0:
                for w in c:
                    contentdbpLIST.append(w[-1])
    posContentdbpSTR = "/".join(contentdbpLIST)
    contentWord_dbp = contentWordPlusPosCounter(posContentdbpSTR)
    print(contentWord_dbp)
    
    contentpbdLIST = []
    for i in range(0, len(pbdSTR), 2000):
        pbdDICT = articut.parse(pbdSTR[i:i+2000])
        contentpbdLIST = articut.getContentWordLIST(pbdDICT)
        for c in contentpbdLIST:
            if len(c) > 0:
                for w in c:
                    contentpbdLIST.append(w[-1])
    posContentpbdSTR = "/".join(contentpbdLIST)
    contentWord_pbd = contentWordPlusPosCounter(posContentpbdSTR)
    print(contentWord_pbd)    
    #將以上所有的 _dbp 都存入 count_result.json 裡
    print(dbpDICT)
    MyjsonName1 = "dbp_count_result.json"
    jsonFileWriter(dbpDICT, MyjsonName1)   
    
    print(pbdDICT)
    MyjsonName2 = "pbd_count_result.json"
    jsonFileWriter(pbdDICT, MyjsonName2) 
