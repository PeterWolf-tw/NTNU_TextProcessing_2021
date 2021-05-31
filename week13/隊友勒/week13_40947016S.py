

import json
from gensim.models import word2vec
from gensim import models




def writeJSON(path, data):
    with open(path, 'w', encoding="utf8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


if __name__== "__main__":
    simLIST = ["電腦","鯊魚","平板","中毒","黑暗","文本","清晰","滑鼠","森林","撲克牌"]
    model = models.Word2Vec.load("wiki2019tw_word2vec_cbow_d300.model")
    result = {}
    for s in simLIST:
        sims = model.wv.most_similar((s), topn=10)
        result[s] = []
        for simWord in sims:
            print("{}, {}".format(simWord[0], str(simWord[1])))
            result[s].append(simWord[0])
        print("\n")
    jsonPath = "wv2_40947016S.json"
    writeJSON(jsonPath,result)

     
    
















