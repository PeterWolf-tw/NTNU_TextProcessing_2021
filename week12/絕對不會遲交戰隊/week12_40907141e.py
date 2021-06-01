#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
from ArticutAPI import Articut

def jsonTextReader(jsonFilePath):
    with open(jsonFilePath, encoding = "utf-8") as f:
        Content = f.read()
    return Content 

def jsonFileWriter(jsonDICT, jsonFileName):
    with open(jsonFileName, mode="w") as f:
        json.dump(jsonDICT, f, ensure_ascii=False)
    return None

def EventAnalysis(inputSTR, nlptool):
    resultDICT = articut.parse(inputSTR, level="lv3")
    return resultDICT

if __name__== "__main__":
    articut = Articut(username = "a0915751010@gmail.com", apikey = "4#-!FX^Vr5kBaznKL2U7egRwkU=Hx*k")  
    fileTUPLE = ("../example/text.txt", "./A. forsteri.txt")
    MouseSTR = jsonTextReader(fileTUPLE[0])
    #print(MouseSTR)
    PenguinSTR = jsonTextReader(fileTUPLE[1])   
    #print(PenguinSTR)
    
    MouseDICT_lv3 = EventAnalysis(MouseSTR, articut)
    MouseLIST = MouseDICT_lv3["event"]

    MouseDICT_lv2 = articut.parse(MouseSTR, level = "lv2")
    MouseLIST_lv2 = articut.getVerbStemLIST(MouseDICT_lv2)    
    #for item in MouseLIST_lv2:
    #    if item != '\n' and item != []:
    #        print(item)  
    
    PenguinDICT_lv3 = EventAnalysis(PenguinSTR, articut)
    PenguinLIST = PenguinDICT_lv3["event"]
    
    ResultDICT = {"倉鼠":[], "皇帝企鵝":[]}
    for item in MouseLIST:
        if item != '\n' and item != []:
            ResultDICT["倉鼠"].append(item)
    for item in PenguinLIST:
        if item != '\n' and item != []:
            ResultDICT["皇帝企鵝"].append(item)
    print(ResultDICT)
    MyjsonName = "week12_絕對不會遲交戰隊_40775012H.json"
    jsonFileWriter(ResultDICT, MyjsonName)       