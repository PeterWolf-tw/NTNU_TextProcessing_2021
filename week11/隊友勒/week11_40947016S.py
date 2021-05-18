#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 把 week11.py 改名為  week11_分組隊名.py 放入你的隊名目錄中
# 在 week11_分組隊名.py 中，設計你的程式，利用 Jieba/CKIPTagger/Articut 任選一種 NLP 工具完成以下指定規格：
# 把 "dbp.txt" 和 "pbd.txt" 的內容取出進行詞頻計算。

# 請仔細觀察前述兩兩一組的 _dbp vs. _pbd 的結果，並小組討論「是否能從詞頻裡分辨究竟哪一篇是人咬狗，哪一篇是狗咬人？。若能，是為什麼，若不能，又是為什麼。」討論結果請另存成 discussion_分隊隊名.txt 一併上傳到課程 week11 的 repo 裡。
from ArticutAPI import ArticutAPI
import json

def txt2Str(path):
    with open(path, encoding="utf-8")as f:
        str = f.read()
    return str

def writeJSON(path, data):
    with open(path, 'w', encoding="utf8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def termFreq(wordLIST):
    r= {}
    for word in wordLIST:
        if word not in r:
            r[word] = 1
        else:
            r[word] += 1
    return r
def posFreq(wordLIST):
    r= {}
    posLIST = []
    for objLIST in wordLIST["result_obj"]:
        for obj in objLIST:
            posLIST.append("<{0}>{1}</{0}>".format(obj["pos"], obj["text"]))
    for word in posLIST:
        if word not in r:
            r[word] = 1
        else:
            r[word] += 1
    return r
def chaFreq(wordSTR):
    r= {}
    for word in wordSTR:
        if word not in r:
            r[word] = 1
        else:
            r[word] += 1
    return r
def articut2LIST(wordLIST):
    r= []
    for item in wordLIST:
        for words in item:
            try:    
                r.append(words[2])
            except:
                print(words)
    return r

def wordFreq(wordLIST):
    r = {}
    splitLIST =  wordLIST["result_segmentation"].split("/")
    for word in splitLIST:
        if word not in r:
            r[word] = 1
        else:
            r[word] += 1
    return r
def json2DictReader(jsonFilePath):
    file = open(jsonFilePath, encoding="utf8")
    DICT = json.loads(file.read())
    return DICT


if __name__== "__main__":
    APIinfo = "account40947016S.info"
    LIST = json2DictReader(APIinfo)
    email = LIST["email"]
    API = LIST["API"]
    articut = ArticutAPI.Articut(username=email, apikey=API)

    dbpPath = "../example/dbp.txt"
    pbdPath = "../example/pbd.txt"
    dbpSTR = txt2Str(dbpPath)
    pbdSTR = txt2Str(pbdPath)
    # 計算兩文本的「字符」出現次數 (如同本簡報 p8 上半頁)，並存成 charCount_dbp 和 charCount_pbd
    charCount_dbp = chaFreq(dbpSTR)
    charCount_pbd = chaFreq(pbdSTR)
    # 計算兩文本的「字詞」出現次數 (如同本簡報 p8 下半頁)，並存成 wordCount_dbp 和 wordChount_pbd
    dbpPOS = articut.parse(dbpSTR)
    pbdPOS = articut.parse(pbdSTR)
    dbpLIST = articut.getContentWordLIST(dbpPOS)
    pbdLIST = articut.getContentWordLIST(pbdPOS)
    wordCount_dbp = wordFreq(dbpPOS)
    wordCount_pbd = wordFreq(pbdPOS)
    # 計算兩文本含有詞性標記的字詞出現次數 (如本簡報 p9)，並存成 posWordCount_dbp 和 posWordCount_pbd
    posWordCount_dbp = posFreq(dbpPOS)
    posWordCount_pbd = posFreq(pbdPOS)
    # 計算兩文本「去除功能詞」(如本簡報 p10)，並存成 contentWord_dbp 和 contentWord_pbd 
    contentWord_dbp =termFreq(articut2LIST(dbpLIST))
    contentWord_pbd =termFreq(articut2LIST(pbdLIST))
    # 將以上所有的 _dbp 都存入 count_result.json 裡
    result = {"charCount_dbp":charCount_dbp,"charCount_pbd":charCount_pbd,"wordCount_dbp":wordCount_dbp,"wordCount_pbd":wordCount_pbd,"posWordCount_dbp":posWordCount_dbp,"posWordCount_pbd":posWordCount_pbd,"contentWord_dbp":contentWord_dbp,"contentWord_pbd":contentWord_pbd}
    p = "count_result.json"
    writeJSON(p,result)


    
