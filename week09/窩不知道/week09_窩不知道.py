#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import json
import requests
from ArticutAPI import ArticutAPI





def json2DictReader(jsonFilePath):
    #設計一個把 .json 檔開啟成 DICT 的函式
        with open(jsonFilePath, encoding="utf-8") as f:
            returnDICT = f.read()
        returnDICT = json.loads(returnDICT)
        return returnDICT


def termFreq(wordLIST):
    r = {}
    for word in wordLIST:
        if word not in r:
            r[word] = 1
        else:
            r[word] += 1
    return r

def jsonFileWriter(jsonDICT, jsonFileName):
    with open(jsonFileName, mode="w", encoding="utf-8") as f:
        json.dump(jsonDICT, f, ensure_ascii=False)
    return None


if __name__ == "__main__":
    #讀入 account.info 檔，並將內容的 email 和 apikey 輸入 Articut() 做為帳號資訊
    userDICT = json2DictReader("account.info")
    username = userDICT["email"]
    apikey = userDICT["API"]
    articut = ArticutAPI.Articut(username, apikey)


    # 把 "tourblog.json" 中的「行政地名」和「景點名稱」取出，
    # 另存入兩個 LIST，再將這兩個 LIST 存成 tourblog_geoinfo.json 檔。
    # 內容為 {"location": [....], "place":[....]}
    tourblogContent = json2DictReader("../example/tourblog.json")
    resultDICT = articut.parse(tourblogContent)
    locationLIST = articut.getLocationStemLIST(resultDICT)
    resultDICT = articut.parse(tourblogContent, openDataPlaceAccessBOOL=True)
    placeLIST = articut.getOpenDataPlaceLIST(resultDICT)
    jsonFileWriter({"location": locationLIST, "place": placeLIST}, "./tourblog_geoinfo.json")


    # 把 "刑事判決_106,交簡,359_2017-02-21.json" 中 "mainText" 欄位裡的刑罰取出，
    # 另存為 justice.json檔，內容為 {"liability": "<你取出的刑罰>"}。
    justiceTEXT = json2DictReader('../example/刑事判決_106,交簡,359_2017-02-21.json')
    from ArticutAPI import ArticutAPI
    lawTK = ArticutAPI.LawsToolkit(justiceTEXT)
    resultDICT = articut.parse(justiceTEXT, level = "lv2")
    lawLIST = lawTK.getLawArticle()
    jsonFileWriter({"liability": lawLIST}, "./justice.json")


    # 把 "news.json" 中 "content" 中的：
    #人名列出，並計算每個人名出現的次數
    #地點列出
    #涉案金額列出
    #將以上資訊另存為 news_info.json 檔，內容為 {"people":[(人名, 次數), (人名, 次數),...], "location":[...], "money":[...]}
    newsContent = json2DictReader("../example/news.json")
    resultDICT = articut.parse(newsContent, level = "lv2")
    nameLIST = articut.getPersonLIST(resultDICT)
    locLIST = articut.getLocationStemLIST(resultDICT)
    monLIST = articut.getCurrencyLIST(resultDICT)
    freqLIST = termFreq(nameLIST)
    jsonFileWriter({"people": [(nameLIST,freqLIST)], "location": locLIST, "money": monLIST}, "./news_info.json")

