import nltk
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import json
import re
'''
那我就線上掛著...嗎 你們可以隨時來編輯之類的
'''

# 放棄 我決定還是一個檔案好了

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
	for i in ( "、", "，", "。", ",",";","；",'"',"'", '“'):
		inputSTR = inputSTR.replace( i, "<MyCuttingMark@CSIE112>")
	for i in range(len(inputSTR)):
		if inputSTR[i] == " ":
			if re.match( r"[0-9] [0-9]", inputSTR[i-1:i+2]):
				inputSTR = inputSTR[0:i] + ',' + inputSTR[i+1:]
	inputLIST = inputSTR.split("<MyCuttingMark@CSIE112>")
	return inputLIST[:-1]


def sentence2Words(inputSTRLIST):
	resultLIST = []
	for s in inputSTRLIST:
		resultLIST.extend( s.split(' '))
	for i in resultLIST:
		if i == '':
			resultLIST.remove(i)
	return resultLIST

def jsonFileWriter(jsonDICT, jsonFileName):
	"""轉換 jsonDICT 為 json 格式的檔案，並存檔。檔名由 jsonFileName 指定。"""
	with open(jsonFileName, mode="w", encoding="utf-8") as f:
		json.dump(jsonDICT, f, ensure_ascii=False)
	return None

if __name__ == "__main__":


	#把 "foxnews.json" 中的 "content" 取出成為字串 foxnewsSTR
	#把 json 的 DICT 保存下來方便後續處理
	jsonDICT = json2DictReader( "../example/foxnews.json")
	foxnewsSTRb = jsonDICT["content"]

	#把 foxnewsSTR 依序斷句存成 foxsentenceLIST，寫回 foxnews.json 中；斷詞存成 foxwordLIST 寫回 foxnews.json 中；POS 處理存成 foxPOS 寫回 foxnews.json 中；NER 處理成 foxNER 寫回 foxnews.json 中。全部完成以後，請確認你的 foxnews.json 是可以被順利開啟讀取的。

	#把 foxnewsSTR 依序斷句存成 foxsentenceLIST，暫時放入 jsonDICT
	foxsentenceLIST = text2Sentence( foxnewsSTRb)
	jsonDICT["foxsentenceLIST"] = foxsentenceLIST
	# print( foxsentenceLIST)

	#把斷詞存成 foxwordLIST，暫時放入 jsonDICT
	foxwordLIST = sentence2Words( foxsentenceLIST)
	jsonDICT["foxwordLIST"] = foxwordLIST
	print( foxwordLIST)
	
	#POS 處理存成 foxPOS，暫時放入 jsonDICT
	foxPOS = nltk.pos_tag(foxwordLIST)
	jsonDICT["foxPOS"] = foxPOS
	# print(foxPOS)

	#NER 處理成 foxNER，暫時放入 jsonDICT
	#TODO
	foxNER = nltk.ne_chunk(foxPOS)
	jsonDICT["foxNER"] = foxNER
	# print( foxNER)

	#把 jsonDICT 寫回 foxnews.json 中
	jsonFileWriter( jsonDICT, "./foxnews.json");



''' 這邊都是上課的內容
	# inputSTR01 = """I went to Japan. (NOT I went to the Japan.)He played tennis with Ben. (NOT He played tennis with the Ben.)They had breakfast at 9 o’clock. (NOT They had a breakfast at 9 o'clock.)(Some words don't have an article. We don't usually use articles for countries, meals or people.)"""
	# sentenceLIST = nltk.sent_tokenize(inputSTR01)
	# print( sentenceLIST )

	# lemm = WordNetLemmatizer()
	# stem = PorterStemmer()

	# inputWord = "communication"
	# print(lemm.lemmatize(inputWord))
	# print(stem.stem(inputWord))
	# inputWord = "loneliness"
	# print(lemm.lemmatize(inputWord))
	# print(stem.stem(inputWord))

	# wordLIST = []
	# for s in sentenceLIST:    
	# 	wordLIST.extend(nltk.word_tokenize(s))
	# contentLIST = []
	# for w in wordLIST:    
	# 	if w.lower() in stopwords.words("english"):
	# 		contentLIST.append("□"*len(w))
	# 	else:        
	# 		contentLIST.append(w)
	# print(" ".join(contentLIST))
	# posLIST = nltk.pos_tag(wordLIST)
	# print(posLIST)
'''
