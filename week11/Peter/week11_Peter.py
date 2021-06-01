#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 把 week11.py 改名為  week11_分組隊名.py 放入你的隊名目錄中
# 在 week11_分組隊名.py 中，設計你的程式，利用 Jieba/CKIPTagger/Articut 任選一種 NLP 工具完成以下指定規格：
# 把 "dbp.txt" 和 "pbd.txt" 的內容取出進行詞頻計算。
# 計算兩文本的「字符」出現次數 (如同本簡報 p8 上半頁)，並存成 charCount_dbp 和 charCount_pbd
# 計算兩文本的「字詞」出現次數 (如同本簡報 p8 下半頁)，並存成 wordCount_dbp 和 wordChount_pbd
# 計算兩文本含有詞性標記的字詞出現次數 (如本簡報 p9)，並存成 posWordCount_dbp 和 posWordCount_pbd
# 計算兩文本「去除功能詞」(如本簡報 p10)，並存成 contentWord_dbp 和 contentWord_pbd 
# 將以上所有的 _dbp 都存入 count_result.json 裡
# 請仔細觀察前述兩兩一組的 _dbp vs. _pbd 的結果，並小組討論「是否能從詞頻裡分辨究竟哪一篇是人咬狗，哪一篇是狗咬人？。若能，是為什麼，若不能，又是為什麼。」討論結果請另存成 discussion_分隊隊名.txt 一併上傳到課程 week11 的 repo 裡。
import json,sys
sys.path.append("../../week09/SedNeoCat/")
from ArticutAPI import ArticutAPI

def jsonFileWriter(jsonDICT, jsonFileName):
    with open (jsonFileName, mode = "w") as f:
        json.dump(jsonDICT, f, ensure_ascii = False)

def charCounter(inputSTR):
    '''計算「字符」出現次數'''
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


def wordCounter(inputSTR):
    '''計算「字詞」出現次數'''
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


def wordPlusPosCounter(inputSTR):
    '''計算「字詞 + 詞性」出現次數'''
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

def contentWordPlusPosCounter(inputSTR):
    '''計算「內容字詞」(非功能字/詞)出現次數'''
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

if __name__=="__main__":
    with open ("../example/dbp.txt", encoding="utf-8")as f:
        dbpSTR = f.read()
    with open ("../example/pbd.txt", encoding="utf-8")as f:
        pbdSTR = f.read()
    
    charCount_dbp = charCounter(dbpSTR)
    charCount_pbd = charCounter(pbdSTR)

    articut = ArticutAPI.Articut()

    seg_dbpSTR = ""
    for i in range(0, len(dbpSTR), 2000):
        resultDICT = articut.parse(dbpSTR[i:i+2000])
        seg_dbpSTR = seg_dbpSTR + resultDICT['result_segmentation']
    wordCount_dbp = wordCounter(seg_dbpSTR)
    
    seg_pbdSTR = ""
    for i in range(0, len(pbdSTR), 2000):
        resultDICT = articut.parse(pbdSTR[i:i+2000])
        seg_pbdSTR = seg_pbdSTR + resultDICT["result_segmentation"]
    wordCount_pbd = wordCounter(seg_pbdSTR)

    pos_dbpLIST = []
    for i in range(0, len(dbpSTR), 2000):
        resultDICT = articut.parse(dbpSTR[i:i+2000])
        pos_dbpLIST.extend(resultDICT["result_pos"])
    pos_dbpSTR = "".join([p for p in pos_dbpLIST if len(p) > 1])
    posWordCount_dbp = wordPlusPosCounter(pos_dbpSTR)
    
    pos_pbdLIST = []
    for i in range(0, len(pbdSTR), 2000):
        resultDICT = articut.parse(pbdSTR[i:i+2000])
        pos_pbdLIST.extend(resultDICT["result_pos"])
    pos_pbdSTR = "".join([p for p in pos_pbdLIST if len(p) > 1])
    posWordCount_pbd = wordPlusPosCounter(pos_pbdSTR)    

    content_dbpLIST = []
    for i in range(0, len(dbpSTR), 2000):
        resultDICT = articut.parse(dbpSTR[i:i+2000])
        contentLIST = articut.getContentWordLIST(resultDICT)
        for c in contentLIST:
            if len(c) > 0:
                for w in c:
                    content_dbpLIST.append(w[-1])
    posContent_dbpSTR = "/".join(content_dbpLIST)
    contentWord_dbp = contentWordPlusPosCounter(posContent_dbpSTR)

    content_pbdLIST = []
    for i in range(0, len(pbdSTR), 2000):
        resultDICT = articut.parse(pbdSTR[i:i+2000])
        contentLIST = articut.getContentWordLIST(resultDICT)
        for c in contentLIST:
            if len(c) > 0:
                for w in c:
                    content_pbdLIST.append(w[-1])
    posContent_pbdSTR = "/".join(content_pbdLIST)
    contentWord_pbd = contentWordPlusPosCounter(posContent_pbdSTR)
    
    jsonDICT = {
        "charCount_dbp": charCount_dbp,
        "charCount_pbd": charCount_pbd,
        "wordCount_dbp":wordCount_dbp,
        "wordCount_pbd": wordCount_pbd,
        "posWordCount_dbp":posWordCount_dbp,
        "posWordCount_pbd":posWordCount_pbd,
        "contentWord_dbp": contentWord_dbp,
        "contentWord_pbd": contentWord_pbd
    }
    print("dbp_contentword_count: ", jsonDICT["contentWord_dbp"])
    print()
    print("pbd_contentword_count: ", jsonDICT["contentWord_pbd"])
    jsonFileName = "count_result.json"
    jsonFileWriter(jsonDICT, jsonFileName) 
