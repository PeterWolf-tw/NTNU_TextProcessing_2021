import re

# 讀取 json
def json2DictReader(jsonFilePath):
	with open(jsonFilePath, encoding = "utf-8") as f :
		returnDICT = f.read()
	returnDICT = json.loads(returnDICT)
	return returnDICT
	'''
	設計一個把 .json 檔開啟成 DICT 的函式
	'''


#將字串轉為「句子」列表的程式
def text2Sentence(inputSTR):
	for i in ("...", "…"):
		inputSTR = inputSTR.replace( i, "")
	for i in range(len(inputSTR)):
		if inputSTR[i] == ",":
			if  re.match( r"[0-9],[0-9]", inputSTR[i-1:i+2]):
				inputSTR = inputSTR[0:i] + ' ' + inputSTR[i+1:] 
	for i in ( "、", "，", "。", ",",";","；"):
		inputSTR = inputSTR.replace( i, "<MyCuttingMark@CSIE112>")
	for i in range(len(inputSTR)):
		if inputSTR[i] == " ":
			if re.match( r"[0-9] [0-9]", inputSTR[i-1:i+2]):
				inputSTR = inputSTR[0:i] + ',' + inputSTR[i+1:]
	inputLIST = inputSTR.split("<MyCuttingMark@CSIE112>")
	return inputLIST[:-1]

def jsonFileWriter(jsonDICT, jsonFileName):
	"""轉換 jsonDICT 為 json 格式的檔案，並存檔。檔名由 jsonFileName 指定。"""
	with open(jsonFileName, mode="w", encoding="utf-8") as f:
		json.dump(jsonDICT, f, ensure_ascii=False)
	return None