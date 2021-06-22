#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json,os
from pprint import pprint
from ArticutAPI import ArticutAPI
articut = ArticutAPI.Articut()

#讀取 .txt 的程式
def textRead(txtFilepath):
    with open(txtFilepath,encoding = "utf-8") as f:
        inputtext = f.read()
    return inputtext

#寫入 .json 的程式
def jsonWrite(result_DICT,jsonFilename):
    with open(jsonFilename,mode = "w",encoding = "utf-8") as f:
        json.dump(result_DICT,f,ensure_ascii=False)
    return None
#切割字串為列表的程式
def STRcut(inputSTR,STRtype):
    STR_LIST = []
    start = 0
    for i in range(0,len(inputSTR)):    
        if (inputSTR[i] == "/")&(STRtype == 1):
            STR_LIST.append(inputSTR[start:i])
            start = i+1
        elif (inputSTR[i:i+2] == "><")&(STRtype == 2):
            STR_LIST.append(inputSTR[start:i+1])
            start = i+1
    return STR_LIST

#計算每一單詞出現次數
def mainCount(inputLIST):
    word_LIST = []
    for word in inputLIST:
        findyou = 0
        for key in word_LIST:
            if (word == key[0]):
                key[1] = key[1]+1
                findyou = 1
                break
        if (findyou == 0):
            word_LIST.append([word,1])
    return word_LIST

def charCount(inputSTR):
    char_LIST = []
    for i in range(0,len(inputSTR)):
        char_LIST.append(inputSTR[i])
    char_result = mainCount(char_LIST)
    return char_result

def wordCount(inputSTR):
    word_LIST = STRcut(inputSTR,STRtype = 1)
    word_result = mainCount(word_LIST)
    word_result.sort(reverse = True, key = lambda s: s[1])
    return word_result

def posWordCount(inputLIST):
    posWord_LIST = []
    for sentence in inputLIST:
        posWord_LIST.extend(STRcut(sentence,STRtype = 2))
    posWord_result = mainCount(posWord_LIST)
    posWord_result.sort(reverse = True, key = lambda s: s[1])
    return posWord_result

def contentWordCount(inputLIST):
    contentWord_LIST = []
    for i in inputLIST:
        if (i != []):
            for j in i:
                contentWord_LIST.append(j[2])
    contentWord_result = mainCount(contentWord_LIST)
    contentWord_result.sort(reverse = True, key = lambda s: s[1])
    return contentWord_result

#-----------------------程式進入點------------------------<
if __name__== "__main__":
    #設定 .txt 路徑
    filePath = "../example/dbp.txt"
    #讀取 .txt
    inputtext = textRead(filePath)
    #使用 articut 斷詞
    inputtext_Articut = articut.parse(inputtext,level = "lv2")
    #
    charCount_dbp = charCount(inputtext)
    wordCount_dbp = wordCount(inputtext_Articut["result_segmentation"])
    posWordCount_dbp = posWordCount(inputtext_Articut["result_pos"])
    contentWord_dbp = contentWordCount(articut.getContentWordLIST(inputtext_Articut))

    #設定 .txt 路徑
    filePath = "../example/pbd.txt"
    #讀取 .txt
    inputtext = textRead(filePath)
    #使用 articut 斷詞
    inputtext_Articut = articut.parse(inputtext,level = "lv2")
    #
    charCount_pbd = charCount(inputtext)
    wordCount_pbd = wordCount(inputtext_Articut["result_segmentation"])
    posWordCount_pbd = posWordCount(inputtext_Articut["result_pos"])
    contentWord_pbd = contentWordCount(articut.getContentWordLIST(inputtext_Articut))  
    result_DICT = {
                    'charCount_dbp':charCount_dbp,
                    'wordCount_dbp':wordCount_dbp,
                    'posWordCount_dbp':posWordCount_dbp,
                    'contentWord_dbp':contentWord_dbp,
                    'charCount_pbd':charCount_pbd,
                    'wordCount_pbd':wordCount_pbd,
                    'posWordCount_pbd':posWordCount_pbd,
                    'contentWord_pbd':contentWord_pbd
                  }
    jsonFilename = "count_result.json"
    jsonWrite(result_DICT,jsonFilename)
