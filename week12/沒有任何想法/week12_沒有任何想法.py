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

#-----------------------程式進入點------------------------<
if __name__== "__main__":
    event_DICT = {}
    #設定 .txt 路徑
    filePath = "../example/text.txt"
    inputText = textRead(filePath)
    #使用 Articut
    inputText_Articut_DICT = articut.parse(inputText,level = "lv3")
    eventLIST = []
    for event in inputText_Articut_DICT["event"]:
        if (event != []):
            eventLIST.append(event)
    event_DICT["倉鼠"] = eventLIST

    #設定 .txt 路徑
    filePath = "./penguin.txt"
    inputText = textRead(filePath)
    #使用 Articut
    inputText_Articut_DICT = articut.parse(inputText,level = "lv3")
    eventLIST = []
    for event in inputText_Articut_DICT["event"]:
        if (event != []):
            eventLIST.append(event)
    event_DICT["皇帝企鵝"] = eventLIST

    #寫入 .json
    jsonWrite(event_DICT,"week12_沒有任何想法.json")
    pprint(event_DICT)

    
    
