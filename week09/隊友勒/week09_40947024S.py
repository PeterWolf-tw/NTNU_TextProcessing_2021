#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
from ArticutAPI import ArticutAPI


def writeJSON(path, data):
    with open(path, 'w', encoding="utf8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def json2DictReader(jsonFilePath):
    file = open(jsonFilePath, encoding="utf8")
    DICT = json.loads(file.read())
    return DICT


def termFreq(wordLIST):
    r = {}
    for word in wordLIST:
        if word not in r:
            r[word] = 1
        else:
            r[word] += 1
    return r


def removeEmptyList(LIST):
    reLIST = [x[0][2] for x in LIST if x != []]
    return reLIST


if __name__ == "__main__":
    APIinfo = "account40947024S.info"
    LIST = json2DictReader(APIinfo)
    email = LIST["email"]
    API = LIST["API"]
    articut = ArticutAPI.Articut(username = email,apikey=API)
    newspath = "../example/news.json"
    newsDICT = json2DictReader(newspath)
    reDICT = articut.parse(newsDICT["content"])
    personLIST = articut.getPersonLIST(reDICT)
    locLIST = articut.getLocationStemLIST(reDICT)
    moneyLIST = articut.getCurrencyLIST(reDICT)
    locLIST = removeEmptyList(locLIST)
    personLIST = removeEmptyList(personLIST)
    moneyLIST = removeEmptyList(moneyLIST)
    freqLIST = termFreq(personLIST)
    writeloc = "news_info.json"
    newsJSON = {"people": freqLIST, "location": locLIST, "moeny": moneyLIST}
    writeJSON(writeloc, newsJSON)