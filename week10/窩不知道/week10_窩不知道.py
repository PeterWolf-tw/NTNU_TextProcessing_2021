# -*- coding: utf-8 -*-

import json
from pprint import pprint
import re
import nltk

def json2DictReader(jsonFilePath):
	with open(jsonFilePath, encoding = "utf-8") as f :
		returnDICT = f.read()
	returnDICT = json.loads(returnDICT)
	return returnDICT

def jsonFileWriter(jsonDICT, jsonFileName):
    with open(jsonFileName, mode="w", encoding="utf-8") as f:
        json.dump(jsonDICT, f, ensure_ascii=False)
    return None

if __name__ == "__main__":
    
    '''
    把 "foxnews.json" 中的 "content" 取出成為字串 foxnewsSTR
    把 foxnewsSTR 依序斷句存成 foxsentenceLIST，寫回 foxnews.json 中；
    斷詞存成 foxwordLIST 寫回 foxnews.json 中；
    POS 處理存成 foxPOS 寫回 foxnews.json 中；
    NER 處理成 foxNER 寫回 foxnews.json 中。
    全部完成以後，請確認你的 foxnews.json 是可以被順利開啟讀取的。
    '''
    
    #把 "foxnews.json" 中的 "content" 取出成為字串 foxnewsSTR
    foxnewsDICT = json2DictReader("foxnews.json")
    foxnewsSTR = foxnewsDICT["content"]
    
    #把 foxnewsSTR 依序斷句存成 foxsentenceLIST，寫回 foxnews.json 中
    foxsentenceLIST = nltk.sent_tokenize(foxnewsSTR)
    foxnewsDICT["foxsentenceLIST"] = foxsentenceLIST
    
    #斷詞存成 foxwordLIST 寫回 foxnews.json 中
    foxwordLIST = []
    for s in foxsentenceLIST:
        foxwordLIST.extend(nltk.word_tokenize(s))
    foxnewsDICT["foxwordLIST"] = foxwordLIST
    
    #POS 處理存成 foxPOS 寫回 foxnews.json 中
    foxPOS = nltk.pos_tag(foxwordLIST)
    foxnewsDICT["foxPOS"] = foxPOS
    
    #NER 處理成 foxNER 寫回 foxnews.json 中
    foxNER = nltk.ne_chunk(foxPOS)
    foxnewsDICT["foxNER"] = foxNER
    
    jsonFileWriter(foxnewsDICT, "foxnews1.json");
    
    