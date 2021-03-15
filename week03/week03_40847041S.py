#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json

def textReadAndPrint(txtFILE):
    """讀入指定的純文字 txtFILE 檔案路徑，並回傳該檔案的內容。"""
    with open(txtFILE, encoding="utf-8") as f:S
        txtContent = f.read()
    return txtContent

def jsonFileWriter(jsonDICT, jsonFileName):
    """轉換 jsonDICT 為 json 格式的檔案，並存檔。檔名由 jsonFileName 指定。"""
    with open(jsonFileName, "w", encoding="utf-8") as f:
        json.dump(jsonDICT, f, ensure_ascii=False)
    return None

if __name__ == "__main__":
    txtFilePath = "./example/sample.txt"
    txt = textReadAndPrint(txtFilePath)
    splitTxt = txt.split("\n");
    print("讀到原始輸入字串：{}\n\n".format(splitTxt))
    jsonDICT = {
    "name": {"zh":"", "en":""},
    "birth": {"year":"", "month":"", "date":""},
    "job": "",
    "language":[],
    "education":[],
    "spouse":""
    }

    jsonDICT["name"]["zh"]      = splitTxt[0].split(" ")[1] #中文名 柯佳嬿
    jsonDICT["name"]["en"]      = " ".join(splitTxt[1].split(" ")[1:]) #英文名 Alice Ko
    jsonDICT["birth"]["year"]   = splitTxt[2].split(" ")[1] #出生 1985 年 1 月 10 日（35歲
    jsonDICT["birth"]["month"]  = splitTxt[2].split(" ")[3] #            ||
    jsonDICT["birth"]["date"]   = splitTxt[2].split(" ")[5] #                  || 
    jsonDICT["job"]             = splitTxt[3].split("\t")[1] #職業	演員
    jsonDICT["language"]        = splitTxt[4].split(" ")[1] #語言 國語、臺語、英語、日語
    jsonDICT["education"]       = splitTxt[5].split(" ")[1] #教育程度 實踐大學應用外語學系肄業、泰北高中、臺北市立蘭雅國民中學、臺北市士林區雨農國民小學
    jsonDICT["spouse"]          = splitTxt[6].split(" ")[1].split("（")[0] #配偶 謝坤達（2017年結婚）

    #上面這個區塊，有個地方讓電腦一直做一樣的事，似乎有讓它更有效率的寫法，不知道有沒有人想到呢？

    print(jsonDICT)
    jsonFileName = "week03_40847041S.json"
    jsonFileWriter(jsonDICT, jsonFileName)

    