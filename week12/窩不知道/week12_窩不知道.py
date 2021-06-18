# -*- coding: utf-8 -*-

import json
from ArticutAPI import ArticutAPI
from pprint import pprint
from requests import post
import re

def articutLogIn(inforpath):
	userDICT = json2DictReader(inforpath)
	username = userDICT["username"]
	apikey = userDICT["apikey"]
	articut = ArticutAPI.Articut( username, apikey)
	return articut

def json2DictReader(jsonFilePath):
	with open(jsonFilePath, encoding = "utf-8") as f :
		returnDICT = f.read()
	returnDICT = json.loads(returnDICT)
	return returnDICT

def txtReader(txtFilePath):
	with open(txtFilePath, encoding = "utf-8") as f :
		returnTXT = f.read()
	return returnTXT

def jsonFileWriter(jsonDICT, jsonFileName):
	"""轉換 jsonDICT 為 json 格式的檔案，並存檔。檔名由 jsonFileName 指定。"""
	with open(jsonFileName, mode="w", encoding="utf-8") as f:
		json.dump(jsonDICT, f, ensure_ascii=False)
	return None

def text2Sentence(inputSTR):
    inputSTR = inputSTR.replace("…", "")
    inputSTR = inputSTR.replace("...", "")
    for i in range(len(inputSTR)):
        if inputSTR[i] == ",":
            if re.match( r"[0-9],[0-9]", inputSTR[i-1:i+2]):
                inputSTR = inputSTR[0:i] + ' ' + inputSTR[i+1:] 
    for item in ("「", "，", "、", "」", "。", "\"", ",", "(", ")"):
        inputSTR = inputSTR.replace(item, "<mark>")
    for i in range(len(inputSTR)):
        if inputSTR[i] == " ":
            if re.match( r"[0-9] [0-9]", inputSTR[i-1:i+2]):
                inputSTR = inputSTR[0:i] + ',' + inputSTR[i+1:]
    inputLIST = inputSTR.split("<mark>")
    return inputLIST[:-1]

def easy2Sentence(inputSTR):
    inputLIST = inputSTR.split("\n")
    for i in inputLIST:
        if i == "":
            inputLIST.remove(i)
    return inputLIST

def addDICT( jsonDICT, key, eventLIST ):
	for i in eventLIST:
		if not (i == '\n' or i == [] ):
			jsonDICT[key].append( tuple(i) )
	return jsonDICT

def jsonFileWriter(jsonDICT, jsonFileName):
	"""轉換 jsonDICT 為 json 格式的檔案，並存檔。檔名由 jsonFileName 指定。"""
	with open(jsonFileName, mode="w", encoding="utf-8") as f:
		json.dump(jsonDICT, f, ensure_ascii=False)
	return None

if __name__== "__main__":
    articut = articutLogIn("account.info")
    resultDICT = {"倉鼠":[], "皇帝企鵝":[]}
    
    #倉鼠
    #lv3event
    mouseSTR = txtReader("text.txt")
    mouseLIST = easy2Sentence(mouseSTR)

    mouseDICTlv3 = articut.parse(mouseSTR, level = "lv3")
    mouseEventLIST = mouseDICTlv3['event']
    #pprint(mouseEventLIST)
    
    resultDICT = addDICT( resultDICT, "倉鼠", mouseEventLIST)
    
    #lv2verb
    mouseDICTlv2 = articut.parse(mouseSTR, level = "lv2")
    mouseVerbLIST = articut.getVerbStemLIST(mouseDICTlv2)
    #pprint(mouseVerbLIST)
    
    #皇帝企鵝
    
    penguinSTR = txtReader("penguin.txt")
    penguinLIST = easy2Sentence(penguinSTR)
    penguinDICTlv3 = articut.parse(penguinSTR, level = "lv3")
    penguinEventLIST = penguinDICTlv3['event']
    resultDICT = addDICT(resultDICT, "皇帝企鵝", penguinEventLIST)
    print(resultDICT)
    
    jsonFileWriter(resultDICT, "week12_窩不知道.json")
    
