#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from gensim.models import word2vec
from gensim import models
import json

if __name__ == "__main__":
    simLIST = ["睡覺","綠茶","可愛","運動","決定","生日","冷藏","下雨","動物","飲料"]
    simDC = {}
    model = models.Word2Vec.load("wiki2019tw_word2vec_cbow_d300.model") #請適度調整你的模型目錄位置
    for s in simLIST:
        simResult = model.wv.most_similar((s),topn = 10)
        for simWord in simResult:
            print("{}, {}".format(simWord[0], str(simWord[1])))
        simDC[s] =[simWord[0] for simWord in simResult] 
        print('\n')
    print(simDC)
    with open('w2v_Peter.json', 'w', encoding='utf-8') as f:
        json.dump(simDC, f,ensure_ascii=False)
