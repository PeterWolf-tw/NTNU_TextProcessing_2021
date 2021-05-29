#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import nltk, json

def jsonFileWriter(jsonDICT, jsonFileName):
    with open(jsonFileName, mode="w") as f:
        json.dump(jsonDICT, f, ensure_ascii=False)
    return None

def CutSentence(inputSTR):
    sentenceLIST = nltk.sent_tokenize(inputSTR)
    return sentenceLIST

def CutWord(sentenceLIST):
    wordLIST = nltk.word_tokenize(sentenceLIST)
    return wordLIST

def FindPOS(wordLIST):
    posLIST = nltk.pos_tag(wordLIST)
    return posLIST

def FindNER(posLIST):
    nerLIST = nltk.ne_chunk(posLIST)
    return nerLIST

if __name__ == "__main__":
    jsonFilePath = "../example/foxnews.json"                                           
    with open(jsonFilePath, "r", encoding = "utf-8") as f:
        foxnewsDICT = json.load(f)
        foxnewsSTR = foxnewsDICT["content"]
    foxnewsSTR = foxnewsSTR.replace("White House", "美國白宮")

    foxsentenceLIST = CutSentence(foxnewsSTR)
    #print(foxsentenceLIST)    
    foxnewsDICT["sentenceLIST"] = foxsentenceLIST

    foxwordLIST = []
    for s in foxsentenceLIST:
        foxwordLIST.extend(CutWord(s)) 
    #print(foxwordLIST)
    foxnewsDICT["wordLIST"] = foxwordLIST

    foxposLIST= FindPOS(foxwordLIST)
    #print(foxPOS)
    foxnewsDICT["posLIST"] = foxposLIST

    foxnerLIST = FindNER(foxposLIST)
    #print(nerLIST)
    foxnewsDICT["nerLIST"] = foxnerLIST
    
    print(foxnewsDICT)
    MyjsonName = "foxnews.json"
    jsonFileWriter(foxnewsDICT, MyjsonName)   