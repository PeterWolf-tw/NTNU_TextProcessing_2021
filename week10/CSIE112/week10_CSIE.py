import nltk
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import json
import myKitFunct


if __name__ == "__main__":


	#把 "foxnews.json" 中的 "content" 取出成為字串 foxnewsSTR
	#把 json 的 DICT 保存下來方便後續處理
	jsonDICT = json2DictReader( "../example/foxnews,json")
	foxnewsSTRb = jsonDICT["content"]

	#把 foxnewsSTR 依序斷句存成 foxsentenceLIST，寫回 foxnews.json 中；斷詞存成 foxwordLIST 寫回 foxnews.json 中；POS 處理存成 foxPOS 寫回 foxnews.json 中；NER 處理成 foxNER 寫回 foxnews.json 中。全部完成以後，請確認你的 foxnews.json 是可以被順利開啟讀取的。

	#把 foxnewsSTR 依序斷句存成 foxsentenceLIST，暫時放入 jsonDICT
	foxsentenceLIST = text2Sentence( foxnewsSTRb)
	jsonDICT["foxsentenceLIST"] = foxsentenceLIST

	#把斷詞存成 foxwordLIST，暫時放入 jsonDICT
	#TODO
	
	#POS 處理存成 foxPOS，暫時放入 jsonDICT
	#TODO
	
	#NER 處理成 foxNER，暫時放入 jsonDICT
	#TODO
	
	#把 jsonDICT 寫回 foxnews.json 中
	#TODO



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
