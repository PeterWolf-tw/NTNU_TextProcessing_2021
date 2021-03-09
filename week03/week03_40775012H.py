#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json                   #模組

def textReadAndPrint(txtFILE):#自定義工具/函式/方法
    """讀入指定的純文字 txtFILE 檔案路徑，並回傳該檔案的內容。"""
    with open(txtFILE, encoding="utf-8") as f:
        txtContent = f.read() #開啟檔案的第二步
    return txtContent

def jsonFileWriter(jsonDICT, jsonFileName):
    """轉換 jsonDICT 為 json 格式的檔案，並存檔。檔名由 jsonFileName 指定。"""
    with open(jsonFileName, mode="w") as f:
        json.dump(jsonDICT, f, ensure_ascii=False)
    return None

if __name__ == "__main__":                                  #主程式的進入點
    txtFilePath = "./example/sample.txt"                    #欲讀取之檔案的路徑
    txt = textReadAndPrint(txtFilePath)                     #讀到的檔案內容
    print("讀到原始輸入字串：{}\n\n".format(txt.split("\n")))#印出以「換行」切割的字串(元組)
    jsonDICT = {                                            #設有6個元素(名字+內容)的空字典
    "name": {"zh":"", "en":""},                             #左字串、右字典(2個元素)
    "birth": {"year":"", "month":"", "date":""},            #左字串、右字典(3個元素)
    "job": "",                                              #左字串、右字串
    "language":[],                                          #左字串、右列表
    "education":[],                                         #左字串、右列表
    "spouse":""                                             #左字串、右字串
    }
    #將資料放入空字典裡
    #for x in range(0,7):
    #jsonDICT[x] = txt.split("\n")[x]                                                                                
    jsonDICT["name"]["zh"]      = txt.split("\n")[0].split(" ")[1]              #先以「換行」切割，再以「一個空格」切割。
    jsonDICT["name"]["en"]      = " ".join(txt.split("\n")[1].split(" ")[1:])   #用「一個空格」將分開的字串黏起來，從所選的該間隔到結束。
    jsonDICT["birth"]["year"]   = txt.split("\n")[2].split(" ")[1]
    jsonDICT["birth"]["month"]  = txt.split("\n")[2].split(" ")[3]
    jsonDICT["birth"]["date"]   = txt.split("\n")[2].split(" ")[5]
    jsonDICT["job"]             = txt.split("\n")[3].split("\t")[1]             #先以「換行」切割，再以「tab」切割。
    jsonDICT["language"]        = txt.split("\n")[4].split(" ")
    jsonDICT["education"]       = txt.split("\n")[5].split(" ")
    jsonDICT["spouse"]          = txt.split("\n")[6].split(" ")[1].split("（")[0]#先以「換行」切割，再以「一個空格」切割，最後以「左括弧」切割。

    print(jsonDICT)
    jsonFileName = "week03_40775012H.json"
    jsonFileWriter(jsonDICT, jsonFileName)   
