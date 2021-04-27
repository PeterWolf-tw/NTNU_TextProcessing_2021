'''
在week07_你的學號_分組隊名.py中，設計你的程式完成以下指定規格：
a.設計一 func() 名為 "text2cws(jsonFilePath)"，接受參數為一 .json 格式的檔案，
  並讀取 json 檔案中的"BODY" 欄位的字串，加以「斷句」以後，使用 Jieba 斷詞將每個
  句子進行斷詞處理，回傳值為一「斷詞處理後的列表」。
b.設計一 func() 名為 "termFreq(inputLIST)"，接受參數為列表，並依列表內容的「字串元素」
  建立一字典 dict 型別的變數，將每個字串元素視為 key，  整份文件中的，該字串元素出現的次數視為 value。
c.設計一程式進入點，透過前述 "text2cws()" 讀取 example/health/ 中所有檔案的 "BODY" 欄位的值，再透過 termFreq() 計算每個斷詞處理後的字串出現的次數。
d.同樣的步驟，再對 example/finance/ 中所有的檔案再處理一次。
'''

import json
import os
import jieba
import re


#讀取 json "BODY" 欄位的字串→Jieba 斷詞處理→回傳處理後的列表
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

#將字串轉為列表
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


# 字串元素出現次數
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
	print("============health============")
	print(statisticsFolder("./example/health"))
	print("============finance============")
	print(statisticsFolder("./example/finance"))


