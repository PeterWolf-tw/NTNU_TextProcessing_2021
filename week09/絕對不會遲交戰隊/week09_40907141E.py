#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
from ArticutAPI import Articut
from ArticutAPI import ArticutAPI

def jsonTextReader(jsonFilePath, field):
    with open(jsonFilePath, encoding = "utf-8") as f:
        Content = f.read()
    Content = json.loads(Content)
    return Content[field] 

def jsonFileWriter(jsonDICT, jsonFileName):
    with open(jsonFileName, mode="w") as f:
        json.dump(jsonDICT, f, ensure_ascii=False)
    return None

def location(inputDICT):
    temp = articut.getLocationStemLIST(inputDICT)
    locLIST = []
    if(temp != None):
        for i in temp:
            if i != [] and i[0][2] not in locLIST: 
                locLIST.append(i[0][2])    
    return locLIST
    
def scenery(inputDICT):
    temp = articut.getOpenDataPlaceLIST(inputDICT)
    scenLIST = []
    if(temp != None):
        for i in temp:
            if i != [] and i[0][2] not in scenLIST:
                scenLIST.append(i[0][2])        
    return scenLIST
    
def law(inputDICT):
    from ArticutAPI import Articut
    lawTK = ArticutAPI.LawsToolkit(inputDICT)
    lawLIST = lawTK.getLawArticle()    
    #for i in lawLIST:
    #    if i not in ['條']:
    #        lawLIST.append(i)    
    return lawLIST    
    
def name(inputDICT):
    nameLIST = articut.getPersonLIST(inputDICT)
    return nameLIST  
 
def termFreq(inputLIST):
    result = {}
    for word in inputLIST:           
        if word:
            result[word] = result[word] + 1
        else:
            result[word] = 1 
    return result 
    
def money(inputDICT):
    moneyLIST = articut.getCurrencyLIST(inputDICT)
    return moneyLIST

if __name__ == "__main__":
    articut = Articut(username = "a0915751010@gmail.com", apikey = "iuS6_RrzjVqjzMOGUu%c$@neEVPzPX4")    

    FilePathTUPLE = ("../example/tourblog.json" , "../example/刑事判決_106,交簡,359_2017-02-21.json", "../example/news.json")    

    tourblogSTR = jsonTextReader(FilePathTUPLE[0], "content")
    tourblogSTR = tourblogSTR.replace(" ", "")
    #print("讀到字串：{}\n".format(tourblogSTR))
    resultDICT = articut.parse(tourblogSTR, level = "lv2", openDataPlaceAccessBOOL = True)
    locLIST = location(resultDICT)
    #print("讀到列表：{}\n".format(locLIST)) 
    scenLIST = scenery(resultDICT)
    #print("讀到列表：{}\n".format(scenLIST))    
    jsonDICT = {"location": locLIST, "place":scenLIST}      
    jsonFileName = "tourblog_geoinfo.json"
    jsonFileWriter(jsonDICT, jsonFileName)  
    print("讀到字典：{}\n".format(jsonDICT))    

    lawSTR = jsonTextReader(FilePathTUPLE[1], "mainText")
    lawSTR = lawSTR.replace(" ", "")
    lawSTR = lawSTR.replace("\r\n", "")
    #print("讀到字串：{}\n".format(lawSTR))
    resultDICT_2 = articut.parse(lawSTR, level = "lv2")
    lawLIST = law(resultDICT_2)
    #print("讀到列表：{}\n".format(lawLIST)) 
    jsonDICT_2 = {"liabilty": lawLIST}
    jsonFileName_2 = "justice.json"
    jsonFileWriter(jsonDICT_2, jsonFileName_2)  
    print("讀到字典：{}\n".format(jsonDICT_2))

    newsSTR = jsonTextReader(FilePathTUPLE[2], "content")
    newsSTR = newsSTR.replace(" ", "")
    #print("讀到字串：{}\n".format(newsSTR))
    resultDICT_3 = articut.parse(newsSTR, level = "lv2")
    nameLIST = name(resultDICT_3)
    nameCountLIST = termFreq(nameLIST)
    #print("讀到列表：{}\n".format(nameCountLIST))      
    locLIST_3 = location(resultDICT_3)
    #print("讀到列表：{}\n".format(locLIST_3))    
    moneyLIST = money(resultDICT_3)
    #print("讀到列表：{}\n".format(moneyLIST)) 
    jsonDICT_3 = {"people": nameCountLIST, "location":locLIST_3, "money":moneyLIST}
    jsonFileName_3  = "news_info.json"
    jsonFileWriter(jsonDICT_3, jsonFileName_3) 
    print("讀到字典：{}\n".format(jsonDICT_3))