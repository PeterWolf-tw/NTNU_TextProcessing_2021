#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
from ArticutAPI import ArticutAPI
from pprint import pprint
from requests import post

def json2DictReader(jsonFilePath):
    with open(jsonFilePath,encoding="utf-8") as f :
        returnDICT = f.read()
    returnDICT=json.loads(returnDICT)
    return returnDICT
    '''
    設計一個把 .json 檔開啟成 DICT 的函式
    '''

def termFreq(wordLIST):
    mydict = dict()
    for sentence in inputLIST:
        for word in sentence.split("|"):
            if mydict.get(word):
                mydict[word] = mydict.get(word) + 1
            else:
                mydict[word] = 1 
    return mydict
    '''
    設計一個計算 wordLIST 中，每個 word 出現次數的函式
    '''
#讀取 json ，取得對應欄位
def jsonTextReader( jsonFilePath, attribute):
    with open( jsonFilePath, encoding="utf-8") as f:
        jsonContent = f.read()
    jsonContent = json.loads(jsonContent)
    return jsonContent[attribute]

def jsonFileWriter(jsonDICT, jsonFileName):
    """轉換 jsonDICT 為 json 格式的檔案，並存檔。檔名由 jsonFileName 指定。"""
    with open(jsonFileName, mode="w", encoding="utf-8") as f:
        json.dump(jsonDICT, f, ensure_ascii=False)
    return None

def tourblogfunct(inputSTR):
    resultDICT = articut.parse(inputSTR, level = "lv2", openDataPlaceAccessBOOL = True)

    temlist = articut.getOpenDataPlaceLIST(resultDICT)
    placelist = []
    # TODO
    for item in temlist:
        if item != []:
            placelist.append( item[0][2] )
    temlist = articut.getLocationStemLIST(resultDICT)
    locationlist = []
    # TODO
    for item in temlist:
        if item != []:
            locationlist.append( item[0][2] )
    # TODO
    resultDICT = {"lacaion": locationlist, "place": placelist}
    return resultDICT
'''
jsonFilePath: 檔案位置
attribute: 要取得 json 的資料欄位名 
articutdel: 處理檔案要用的function
jsonFileName: 檔案儲存名字
'''
def dealJson( jsonFilePath, attribute, articutdel, jsonFileName):
    # 讀取檔案
    inputSTR = jsonTextReader( jsonFilePath, attribute)

    # 使用 atricutdel 選擇處理用的function
    if articutdel == "__tourblogfunct__":
        resultDICT = tourblogfunct(inputSTR)
    # 寫入檔案
    jsonFileWriter( resultDICT, jsonFileName)
    pprint(resultDICT)

if __name__ == "__main__":
    #讀入 account.info 檔，並將內容的 email 和 apikey 輸入 Articut() 做為帳號資訊
    userDICT = json2DictReader("../account.info")
    username = userDICT["username"]
    apikey = userDICT["apikey"]
    articut = ArticutAPI.Articut( username, apikey)

    # 把 "tourblog.json" 中的「行政地名」和「景點名稱」取出，
    # 另存入兩個 LIST，再將這兩個 LIST 存成 tourblog_geoinfo.json 檔。
    # 內容為 {"location": [....], "place":[....]}

    dealJson( "../example/tourblog.json", "content", "__tourblogfunct__", "tourblog_geoinfo.json")
    
    '''
    # 把 "刑事判決_106,交簡,359_2017-02-21.json" 中 "mainText" 欄位裡的刑罰取出，
    # 另存為 justice.json 檔，內容為 {"liability": "<你取出的刑罰>"}。

    jsonSTR = jsonTextReader( "../example/刑事判決_106,交簡,359_2017-02-21.json", "judgement")
    # TODO
    resultDICT = articut.parse(inputSTR)
    
    # 寫入檔案
    jsonFileWriter( resultDICT, "justice.json.json")
    pprint(resultDICT)

    # 把 "news.json" 中 "content" 中的：
    #    人名列出，並計算每個人名出現的次數
    #    地點列出
    #    涉案金額列出
    #    將以上資訊另存為 news_info.json 檔，內容為 {"people":[(人名, 次數), (人名, 次數),...], "location":[...], "money":[...]}
    jsonSTR = jsonTextReader( "../example/tourblog.json", "content")
    # TODO
    resultDICT = articut.parse(inputSTR, level="lv3", openDataPlaceAccessBOOL="True")
    # 讀取檔案
    jsonFileWriter( resultDICT, "news_info.json.json")
    pprint(resultDICT)
    '''