#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from gensim.models import word2vec
from gensim import models
import json

def jsonFileWriter(jsonDICT, jsonFileName):
    """轉換 jsonDICT 為 json 格式的檔案，並存檔。檔名由 jsonFileName 指定。"""
    with open(jsonFileName, mode="w", encoding="utf-8") as f:
        json.dump(jsonDICT, f, ensure_ascii=False)
    return None

if __name__ == "__main__":

    simLIST = ["無知", "虛構", "關係", "亂七八糟", "旅行", "女朋友", "瓜葛", "走", "陽明山", "水壺"]
    simDICT = {}

    for i in simLIST:
        simDICT[i] = []
    
    model = models.Word2Vec.load("./wiki2019tw_word2vec_cbow_d300.model") #請適度調整你的模型目錄位置

    for s in simLIST:
        simResult = model.wv.most_similar((s),topn = 10)
        for simWord in simResult:
            print("{}, {}".format(simWord[0], str(simWord[1])))
            simDICT[s].append(simWord[0])
        print('\n')
    print(simDICT)

    jsonFileWriter(simDICT, "./w2v_窩不知道.json")
    
    #將上述結果，依作業說明另開一個新檔並儲存起來後，上傳 github 繳交。
