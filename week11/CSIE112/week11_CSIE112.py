#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
from ArticutAPI import ArticutAPI
from pprint import pprint
from requests import post

'''
CODE BY CSIE112
'''

# 把 week11.py 改名為  week11_分組隊名.py 放入你的隊名目錄中
# 在 week11_分組隊名.py 中，設計你的程式，利用 Jieba/CKIPTagger/Articut 任選一種 NLP 工具完成以下指定規格：
# 把 "dbp.txt" 和 "pbd.txt" 的內容取出進行詞頻計算。

def json2DictReader(jsonFilePath):
	with open(jsonFilePath, encoding = "utf-8") as f :
		returnDICT = f.read()
	returnDICT = json.loads(returnDICT)
	return returnDICT

def txtFileReader(txtFilePath):
	'''將.txt檔轉為字串'''
	with open(txtFilePath, encoding="utf-8") as f:
		returnSTR = f.read()
	return returnSTR

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
    inputSTR = inputSTR.replace("><", ">CSIE112_SPLITTER<")
    inputLIST = inputSTR.split("CSIE112_SPLITTER")
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

def except_FUNC_label(inputLIST):
	returnLIST = []
	for i in inputLIST :
		if 'FUNC' not in i[0] :
			returnLIST.append(i) 

def jsonFileWriter(jsonDICT, jsonFileName):
	"""轉換 jsonDICT 為 json 格式的檔案，並存檔。檔名由 jsonFileName 指定。"""
	with open(jsonFileName, mode="w", encoding="utf-8") as f:
		json.dump(jsonDICT, f, ensure_ascii=False)
	return None

if __name__== "__main__":
	userDICT = json2DictReader("../../account.info")
	username = userDICT["username"]
	apikey = userDICT["apikey"]
	articut = ArticutAPI.Articut( username, apikey)

	'''get two string'''
	pbdstr = txtFileReader('../example/pbd.txt')
	dbpstr = txtFileReader('../example/dbp.txt')

# 建立兩個 DICT 存所有結果

	pbdDICT = {}
	dbpDICT = {}

# 計算兩文本的「字符」出現次數 (如同本簡報 p8 上半頁)，並存成 charCount_dbp 和 charCount_pbd
	charCount_pbd = charCounter(pbdstr)
	charCount_dbp = charCounter(dbpstr)

	dbpDICT["charCount_dbp"] = charCount_dbp
	pbdDICT["charCount_pbd"] = charCount_pbd

# 計算兩文本的「字詞」出現次數 (如同本簡報 p8 下半頁)，並存成 wordCount_dbp 和 wordChount_pbd
	tmpDICT = articut.parse(pbdstr)
	if 'result_segmentation' in tmpDICT:
		pbdCuttedstr = tmpDICT['result_segmentation']
	else:
		pbdCuttedstr = ""
	tmpDICT = articut.parse(dbpstr)
	if 'result_segmentation' in tmpDICT:
		dbpCuttedstr = tmpDICT['result_segmentation']
	else:
		dbpCuttedstr = ""
	wordCount_pbd = wordCounter(pbdCuttedstr)
	wordCount_dbp = wordCounter(dbpCuttedstr)

	dbpDICT["wordCount_dbp"] = wordCount_dbp
	pbdDICT["wordCount_pbd"] = wordCount_pbd

# 計算兩文本含有詞性標記的字詞出現次數 (如本簡報 p9)，並存成 posWordCount_dbp 和 posWordCount_pbd
	tmpDICT = articut.parse(pbdstr)
	if 'result_pos' in tmpDICT:
		pbdCuttedList = tmpDICT['result_pos']
	else:
		pbdCuttedList = []
	pbdCuttedstr = "".join([i for i in pbdCuttedList if len(i) > 1])
	posWordCount_pbd = wordPlusPosCounter(pbdCuttedstr)
	
	tmpDICT = articut.parse(dbpstr)
	if 'result_pos' in tmpDICT:
		dbpCuttedList = tmpDICT['result_pos']
	else:
		dbpCuttedList = []
	dbpCuttedstr = "".join([i for i in dbpCuttedList if len(i) > 1])
	posWordCount_dbp = wordPlusPosCounter(dbpCuttedstr)

	dbpDICT["posWordCount_dbp"] = posWordCount_dbp
	pbdDICT["posWordCount_pbd"] = posWordCount_pbd

# 計算兩文本「去除功能詞」(如本簡報 p10)，並存成 contentWord_dbp 和 contentWord_pbd 
	contentWord_dbp = except_FUNC_label(posWordCount_dbp)
	contentWord_pbd = except_FUNC_label(posWordCount_pbd)

	dbpDICT["contentWord_dbp"] = contentWord_dbp
	pbdDICT["contentWord_pbd"] = contentWord_pbd

# 將以上所有的 _dbp 都存入 count_result.json 裡
	jsonFileWriter( dbpDICT, "count_result.json")
	jsonFileWriter( pbdDICT, "count_result_pbd.json")

# 請仔細觀察前述兩兩一組的 _dbp vs. _pbd 的結果，並小組討論「是否能從詞頻裡分辨究竟哪一篇是人咬狗，哪一篇是狗咬人？。若能，是為什麼，若不能，又是為什麼。」討論結果請另存成 discussion_分隊隊名.txt 一併上傳到課程 week11 的 repo 裡。