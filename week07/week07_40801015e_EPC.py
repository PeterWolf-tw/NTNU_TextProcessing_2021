Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>
import json
import os
import jieba
import re

def text2cws(jsonFilePath):
	with open( jsonFilePath, encoding="utf-8") as f:
		jsonContent = f.read()
	jsonContent = json.loads(jsonContent)
	jsonContent = jsonContent["BODY"]
	SentenceList = text2Sentence(jsonContent)
	List = []
	for sentence in SentenceList:
		List.append("|".join(jieba.cut(sentence)))
	return List

def text2Sentence(inputSTR):
    for i in range (len(inputSTR)):
        if inputSTR[i] == ",":
            if re.match( r"[0-9],[0-9]", inputSTR[i-1:i+2]):
                pass
            else :
                inputSTR = inputSTR[:i]+"<MyCuttingMark>"+inputSTR[i+1:]
    for i in ("...","…"):
        inputSTR = inputSTR.replace(i,"")
    for i in ( "、", "，", "。", "：", ":", "；", ";"):
        inputSTR = inputSTR.replace(i,"<MyCuttingMark>")
    output_LIST = inputSTR.split("<MyCuttingMark>")
    return output_LIST[:-1]

def termFreq(inputLIST):
	mydict = dict()
	for sentence in inputLIST:
		for word in sentence.split("|"):
			if mydict.get(word):
				mydict[word] = mydict.get(word) + 1
			else:
				mydict[word] = 1
	return mydict

def statisticsFolder(FolderPath):
	FileList = os.listdir(FolderPath)
	health_list = []
	for file in FileList:
		health_list.append("|".join(text2cws(FolderPath+'/'+file)))
	return termFreq(health_list)


if __name__ == "__main__":

	#health
	print("#health")
	print(statisticsFolder("./example/health"))

	#finance
	print("#finance")
	print(statisticsFolder("./example/finance"))
	
