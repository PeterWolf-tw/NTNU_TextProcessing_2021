#!/usr/bin/env python3
#-- coding:utf-8 --

import json
from ArticutAPI import Articut

with open("../account.info") as f:
    accountDICT = json.loads(f.read())
username=accountDICT["email"]
apikey = accountDICT["apikey"]



#讀取 json 的程式
def jsonTextReader(jsonFilePath):
    with open (jsonFilePath, "r", encoding = "utf8") as f:
        jsonContent = json.load(f)
    return jsonContent

#取得地點列表的程式
def location(inputSTR):
    global username
    global apikey
    articut = Articut(username=username, apikey=apikey)
    resultDICT = articut.parse(inputSTR, level = "lv2")
    locLIST = articut.getLocationStemLIST(resultDICT)
    return locLIST

if __name__== "__main__":

    #設定要讀取的 news.json 路徑
    jsonFilePath = "./tourblog.json"

    #將 tourblog.json 利用 [讀取 json] 的程式打開
    tourblogSTR = jsonTextReader(jsonFilePath)["content"].replace(" ", "")

    #將讀出來的內容字串傳給 [將字串轉為地點列表的程式]的程式，存為 locLIST
    locLIST = location(tourblogSTR)
    print(locLIST)
