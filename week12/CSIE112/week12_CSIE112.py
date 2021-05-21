#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
CODE BY CSIE112
'''
import json
import ArticutAPI 
from pprint import pprint
from requests import post


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

def main(inputSTR, nlptool, levelop):
	resultDICT = articut.parse(inputSTR, level=levelop)
	return resultDICT

def jsonFileWriter(jsonDICT, jsonFileName):
	"""轉換 jsonDICT 為 json 格式的檔案，並存檔。檔名由 jsonFileName 指定。"""
	with open(jsonFileName, mode="w", encoding="utf-8") as f:
		json.dump(jsonDICT, f, ensure_ascii=False)
	return None

#將字串轉為「句子」列表的程式
def text2Sentence(inputSTR):
	for i in ("...", "…"):
		inputSTR = inputSTR.replace( i, "")
	for i in range(len(inputSTR)):
		if inputSTR[i] == ",":
			if  re.match( r"[0-9],[0-9]", inputSTR[i-1:i+2]):
				inputSTR = inputSTR[0:i] + ' ' + inputSTR[i+1:] 
	for i in ( "、", "，", "。", ",",";","；",'"',"'", '“'):
		inputSTR = inputSTR.replace( i, "<MyCuttingMark@CSIE112>")
	for i in range(len(inputSTR)):
		if inputSTR[i] == " ":
			if re.match( r"[0-9] [0-9]", inputSTR[i-1:i+2]):
				inputSTR = inputSTR[0:i] + ',' + inputSTR[i+1:]
	inputLIST = inputSTR.split("<MyCuttingMark@CSIE112>")
	return inputLIST[:-1]

#換行為一句的特殊切句，簡單到不知道為什麼需要額外寫成 funct，可能是為了順便清掉空行
def easy2Sentence(inputSTR):
	inputLIST = inputSTR.split('\n')
	for i in inputLIST:
		if i == '':
			inputLIST.remove(i)
	return inputLIST

# 把 eventLIST 寫入 DICT
def addDICT( jsonDICT, key, eventLIST):
	for i in eventLIST:
		if not (i == '\n' or i == []):
			jsonDICT[key].append( tuple(i))
	return jsonDICT

if __name__== "__main__":

	# 使用 json 指定格式讀取指定路徑的 account.info
	''' json 格式
	{
		"username": ,
		"apikey":
	}
	'''
	articut = articutLogIn("../../account.info")
	
	jsonDICT = {"倉鼠":[], "皇帝企鵝":[]}

	# 處理倉鼠

	inputSTR = txtReader("../example/text.txt")
	inputLIST = easy2Sentence(inputSTR)

	'''
	用 lv3 取得 event
	'''
	puipuiDICT_lv3 = main(inputSTR, articut, "lv3")
	puipuiEventLIST = puipuiDICT_lv3["event"]

	# 倉鼠的知識，存入 json
 	# pprint( puipuiEventLIST )

	jsonDICT = addDICT( jsonDICT, "倉鼠", puipuiEventLIST)
	# print( jsonDICT)
	'''
	用 lv2 切，取得 Verb
	'''
	puipuiDICT_lv2 = main(inputSTR, articut, "lv2")
	puipuiVerbLIST = articut.getVerbStemLIST(puipuiDICT_lv2)
	pprint( puipuiVerbLIST)

	# 處理皇帝企鵝
	
	# TODO


	# 皇帝企鵝的知識，存入 json
	jsonDICT = addDICT( jsonDICT, "皇帝企鵝", penguinEventLIST)
	# 確認沒問題刪掉這行註解下面 print
	print( jsonDICT)

	# 將 jsonDICT 存入 week12_CSIE112.json
	jsonFileWriter( jsonDICT, "./week12_CSIE112.json")