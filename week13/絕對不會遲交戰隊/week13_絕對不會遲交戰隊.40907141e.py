#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from gensim.models import word2vec
from gensim import models
import json

def jsonFileWriter(jsonDICT, jsonFileName):
    with open(jsonFileName, mode="w") as f:
        json.dump(jsonDICT, f, ensure_ascii=False)
    return None

if __name__ == "__main__":

    simLIST = ["貓咪", "老鼠", "湯姆貓", "傑利鼠", "文章", "可愛", "耍帥", "鉛筆", "橡皮擦", "尺"]
    resultDICT = {}
    
    model = models.Word2Vec.load("wiki2019tw_word2vec_cbow_d300.model")

    for s in simLIST:
        simResult = model.wv.most_similar((s),topn = 10)
        for simWord in simResult:
            resultDICT[s].append(simWord[0])
            print("{}, {}".format(simWord[0], str(simWord[1])))
        print('\n')

    print(resultDICT)
    MyjsonName = "w2v_絕對不會遲交戰隊_40907141e.json"
    jsonFileWriter(resultDICT, MyjsonName)  