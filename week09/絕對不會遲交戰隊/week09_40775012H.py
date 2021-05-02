#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
from ArticutAPI import Articut

#設計一個把 .json 檔開啟成 DICT 的函式
def json2DictReader(jsonFilePath):
    with open(jsonFilePath, "r", encoding = "utf8") as f:
        jsonContent = json.load(f)
    return jsonContent    

#設計一個計算 wordLIST 中，每個 word 出現次數的函式
def termFreq(wordLIST):
    result = {}
    for sentence in inputLIST:
        for word in sentence.split("|"):            
            if result.get(word):
                result[word] = result.get(word) + 1
            else:
                result[word] = 1 
    return result

def location(inputSTR):
    global username
    global apikey
    articut = Articut(username = "a0915751010@gmail.com", apikey = "iuS6_RrzjVqjzMOGUu%c$@neEVPzPX4")
    resultDICT = articut.parse(inputSTR, level = "lv2")
    locLIST = articut.getLocationStemLIST(resultDICT)
    return locLIST
    #半成品
def scenery(inputSTR):
    global username
    global apikey
    articut = Articut(username = "a0915751010@gmail.com", apikey = "iuS6_RrzjVqjzMOGUu%c$@neEVPzPX4")
    resultDICT = articut.parse(inputSTR, level = "lv2", openDataPlaceAccessBOOL = True)
    scenLIST = articut.getOpenDataPlaceLIST(resultDICT)
    return scenLIST
    #半成品
def law(inputSTR):
    global username
    global apikey
    articut = Articut(username = "a0915751010@gmail.com", apikey = "iuS6_RrzjVqjzMOGUu%c$@neEVPzPX4")
    for i in ("\r\n"):
        inputSTR = inputSTR.replace(i, "")
    resultDICT = articut.parse(inputSTR, level = "lv2")
    lawTK = ArticutAPI.LawsToolkit(inputDICT)
    lawLIST = lawTK.getLawArticle()
    return lawLIST    
    #半成品
def name(inputSTR):
    global username
    global apikey
    articut = Articut(username = "a0915751010@gmail.com", apikey = "iuS6_RrzjVqjzMOGUu%c$@neEVPzPX4")
    resultDICT = articut.parse(inputSTR, level = "lv2")
    nameLIST = articut.getPersonLIST(resultDICT)
    return nameLIST  
    #半成品
def money(inputSTR):
    global username
    global apikey
    articut = Articut(username = "a0915751010@gmail.com", apikey = "iuS6_RrzjVqjzMOGUu%c$@neEVPzPX4")
    resultDICT = articut.parse(inputSTR, level = "lv2")
    moneyLIST = articut.getCurrencyLIST(resultDICT)
    return moneyLIST

if __name__ == "__main__":
    #讀入 account.info 檔，並將內容的 email 和 apikey 輸入 Articut() 做為帳號資訊
    with open("../account.info") as f:
        accountDICT = json.loads(f.read())
    username = accountDICT["email"]
    apikey = accountDICT["apikey"]

    FilePathTUPLE = ("../example/tourblog.json" , "../example/刑事判決_106,交簡,359_2017-02-21.json", "../example/news.json")

    #將 tourblog.json 利用 [讀取 json] 的程式打開
    tourblogSTR = json2DictReader(FilePathTUPLE[0])["content"].replace(" ", "")
    print("讀到字串：{}\n".format(tourblogSTR))    
    #將讀出來的內容字串傳給 [將字串轉為地點列表的程式]的程式，存為 locLIST   
    locLIST = location(tourblogSTR)   
    scenLIST = scenery(tourblogSTR)
    print("讀到列表：{}\n".format(locLIST))      
    print("讀到列表：{}\n".format(scenLIST))    
    # 內容為 {"location": [....], "place":[....]}  
    jsonDICT = {"location": [], "place":[]}
    # 把 "tourblog.json" 中的「行政地名」和「景點名稱」取出，    
    jsonDICT["location"] = locLIST
    jsonDICT["place"] = scenLIST 
    # 另存入兩個 LIST，再將這兩個 LIST 存成 tourblog_geoinfo.json 檔。    
    jsonFileName = "tourblog_geoinfo.json"
    jsonFileWriter(jsonDICT, jsonFileName)  
    print(jsonDICT)    

    # 把 "刑事判決_106,交簡,359_2017-02-21.json" 中 "mainText" 欄位裡的刑罰取出，
    # 另存為 justice.json檔，內容為 {"liability": "<你取出的刑罰>"}。
    lawSTR = json2DictReader(FilePathTUPLE[1])["content"].replace(" ", "")
    print("讀到字串：{}\n".format(lawSTR))  
    lawLIST = law(lawSTR)
    print("讀到列表：{}\n".format(lawLIST)) 
    jsonDICT_2 = {"liabilty": []}
    jsonDICT_2["liabilty"] = lawLIST
    jsonFileName = "justice.json"
    jsonFileWriter(jsonDICT_2, jsonFileName)  
    print(jsonDICT_2)
    
    # 把 "news.json" 中 "content" 中的：
    #    人名列出，並計算每個人名出現的次數
    #    地點列出
    #    涉案金額列出
    #    將以上資訊另存為 news_info.json 檔，內容為 {"people":[(人名, 次數), (人名, 次數),...], "location":[...], "money":[...]}
    newsSTR = json2DictReader(FilePathTUPLE[1])["content"].replace(" ", "")
    print("讀到字串：{}\n".format(newsSTR))
    jsonDICT_3 = {"people": [], "location":[], "money":[]}
    nameLIST_3 = name(newsSTR)
    
    #半成品
    
    locLIST_3 = location(newsSTR)
    moneyLIST_3 = money(newsSTR)
    print("讀到列表：{}\n".format(nameLIST_3)) 
    print("讀到列表：{}\n".format(locLIST_3)) 
    print("讀到列表：{}\n".format(moneyLIST_3)) 
    jsonDICT_3["people"] = nameLIST_3
    jsonDICT_3["location"] = locLIST_3
    jsonDICT_3["money"] = moneyLIST_3
    jsonFileName = "news_info.json"
    jsonFileWriter(jsonDICT_3, jsonFileName) 
    print(jsonDICT_3)
    