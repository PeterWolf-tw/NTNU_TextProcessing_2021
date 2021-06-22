#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json,jieba,os

#讀取 json 並斷詞的程式
def text2cws(jsonFilepath, target):
    with open(jsonFilepath,encoding="utf-8") as f:
        inputtext = json.load(f)[target]
    sentence_LIST = text2Sentence(inputtext)
    inputword_LIST = []
    for sentence in sentence_LIST:
        word_LIST = jieba.lcut(sentence,cut_all=False,use_paddle=True) #使用 jieba 斷詞
        for word in word_LIST:
            for WTF in ["「","」","(",")","：","（","）",":","【","】","／"]:
                if (word == WTF):
                    word_LIST.remove(word)
        inputword_LIST.extend(word_LIST)
    return inputword_LIST

#將字串轉為「句子」列表的程式
def text2Sentence(inputSTR):
    sentence_LIST = []
    start = 0
    k = 0
    length_STR = len(inputSTR)
    while k < length_STR:
        for i in [".","…"," "]:
            if inputSTR[k]==i:
                inputSTR=inputSTR[:k]+inputSTR[k+1:]
                length_STR=len(inputSTR)
                k = k-1
                break
        k = k+1
    for i in range(0,length_STR):
        number = 0
        if (inputSTR[i]==","):
            for j in range(0,10):
                if((inputSTR[i-1]==str(j))|(inputSTR[i+1]==str(j))):
                    number = number+1
            if (number == 2):
                pass
            else:
                sentence_LIST.append(inputSTR[start:i])
                start = i+1
        for j in ["、","，","。","？","；",";"]:
            if (inputSTR[i]==j):
                sentence_LIST.append(inputSTR[start:i])
                start = i+1
                break
    return sentence_LIST

#計算每一單詞出現次數
def termFreq(inputLIST,target):
    word_DICT = {}
    for word in inputLIST:
        findyou = 0
        for key in word_DICT:
            if (word == key):
                word_DICT[key] = word_DICT[key]+1
                findyou = 1
                break
        if (findyou == 0):
            word_DICT[word] = 1
    return word_DICT

#--------------------程式進入點------------------------<
if __name__== "__main__":
    #設定要讀取的 json 根目錄
    rootPath = "./example/health/"
    target="BODY"
    #對路徑下每個 json 進行處理
    path_STR_LIST = os.listdir(rootPath)
    for STR in path_STR_LIST:
        filePath = os.path.join(rootPath,STR)
        print(STR)
        if (os.path.isfile(filePath)&(STR[len(STR)-5:] == ".json")):
            inputword_LIST = text2cws(filePath,target)
            print("{}".format(termFreq(inputword_LIST,target)))
    #設定要讀取的 json 根目錄
    rootPath = "./example/finance/"
    target="BODY"
    #對路徑下每個 json 進行處理
    path_STR_LIST = os.listdir(rootPath)
    for STR in path_STR_LIST:
        filePath = os.path.join(rootPath,STR)
        print(STR)
        if (os.path.isfile(filePath)&(STR[len(STR)-5:] == ".json")):
            inputword_LIST = text2cws(filePath,target)
            print("{}".format(termFreq(inputword_LIST,target)))
