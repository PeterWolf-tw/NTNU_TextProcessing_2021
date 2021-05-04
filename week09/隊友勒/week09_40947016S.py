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
    APIinfo = "account40947016S.info"
    LIST = json2DictReader(APIinfo)
    email = LIST["email"]
    API = LIST["API"]
    articut = ArticutAPI.Articut(username=email, apikey=API)
    # 讀入 account.info 檔，並將內容的 email 和 apikey 輸入 Articut() 做為帳號資訊
    ''' tourloc = "../example/tourblog.json"
    tourJSON = json2DictReader(tourloc)
    tourSTR = tourJSON["content"]
    reDICT = articut.parse(tourSTR, openDataPlaceAccessBOOL=True)
    placeLIST = articut.getOpenDataPlaceLIST(reDICT)
    locLIST = articut.getLocationStemLIST(reDICT)
    placeLIST = removeEmptyList(placeLIST)
    locLIST = removeEmptyList(locLIST)
    resultJSON = {"location": locLIST, "place": placeLIST}
    writeloc = "tourblog_geoinfo.json"
    writeJSON(writeloc, resultJSON) '''
    # 把 "tourblog.json" 中的「行政地名」和「景點名稱」取出，
    # 另存入兩個 LIST，再將這兩個 LIST 存成 tourblog_geoinfo.json 檔。
    # 內容為 {"location": [....], "place":[....]}

    # 把 "刑事判決_106,交簡,359_2017-02-21.json" 中 "mainText" 欄位裡的刑罰取出，
    # 另存為 justice.json檔，內容為 {"liability": "<你取出的刑罰>"}。
    ''' justicepath = "../example/刑事判決_106,交簡,359_2017-02-21.json"
    justiceDICT = json2DictReader(justicepath)
    reDICT = articut.parse(justiceDICT["judgement"])
    liabilityDICT = ArticutAPI.LawsToolkit(reDICT).getLawArticle()
    liabilityJSON = {"liability": liabilityDICT}
    writeloc = "justice.json"
    writeJSON(writeloc, liabilityJSON) '''

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
    # 把 "news.json" 中 "content" 中的：
    #    人名列出，並計算每個人名出現的次數
    #    地點列出
    #    涉案金額列出
    #    將以上資訊另存為 news_info.json 檔，內容為 {"people":[(人名, 次數), (人名, 次數),...], "location":[...], "money":[...]}
