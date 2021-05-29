#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import warnings
from gensim.models import word2vec
from gensim import models
import json


def jsonFileWriter(jsonDICT, jsonFileName):
	"""轉換 jsonDICT 為 json 格式的檔案，並存檔。檔名由 jsonFileName 指定。"""
	with open(jsonFileName, mode="w", encoding="utf-8") as f:
		json.dump(jsonDICT, f, ensure_ascii=False)
	return None

if __name__ == "__main__":

    simLIST = ["討厭","海豹","躺","好吃","烤","肺炎","紅茶","茶館","綠茶","貓"]
    simDICT = {}
    for i in simLIST:
    	simDICT[i] = []
    model = models.Word2Vec.load("./wiki2019tw_word2vec_cbow_d300/wiki2019tw_word2vec_cbow_d300.model") #請適度調整你的模型目錄位置

    for s in simLIST:
        simResult = model.wv.most_similar((s),topn = 10)
        if simResult is None:
        	print("{} is no result".format(s))
        	continue
        for simWord in simResult:
        	simDICT[s].append(simWord[0])
        	print("{}, {}".format(simWord[0], str(simWord[1])))
        print('\n')
    print(simDICT)
    jsonFileWriter( simDICT, "./w2v_CSIE112.json")

    #將上述結果，依作業說明另開一個新檔並儲存起來後，上傳 github 繳交。
