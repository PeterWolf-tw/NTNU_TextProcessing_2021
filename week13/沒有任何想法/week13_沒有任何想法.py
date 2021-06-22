#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from gensim.models import word2vec
from gensim import models
import json

#寫入 .json 的程式
def jsonWrite(result_DICT,jsonFilename):
    with open(jsonFilename,mode = "w",encoding = "utf-8") as f:
        json.dump(result_DICT,f,ensure_ascii=False)
    return None

if __name__ == "__main__":

    simLIST = ["手機","水壺","跳","情人節","雜貨店","冷氣","就業","交流電","心臟","剪刀"]

    simDICT = {}
    
    model = models.Word2Vec.load("./wiki2019tw_word2vec_cbow_d300/wiki2019tw_word2vec_cbow_d300.model")

    for s in simLIST:
        simResult = model.wv.most_similar((s),topn = 10)
        wordLIST = []
        for simWord in simResult:
            print("{}, {}".format(simWord[0], str(simWord[1])))
            wordLIST.append(simWord[0])
        simDICT[s] = wordLIST
        print('\n')
    print(simDICT)

    jsonWrite(simDICT,"w2v_沒有任何想法.json")
