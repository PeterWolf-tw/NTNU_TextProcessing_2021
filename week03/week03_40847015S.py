#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
import re

def textReadAndPrint(txtFILE):
    """讀入指定的純文字 txtFILE 檔案路徑，並回傳該檔案的內容。"""
    with open(txtFILE, encoding="utf-8") as f:
        txtContent = f.read()
    return txtContent

def jsonFileWriter(jsonDICT, jsonFileName):
    """轉換 jsonDICT 為 json 格式的檔案，並存檔。檔名由 jsonFileName 指定。"""
    with open(jsonFileName, mode="w") as f:
        json.dump(jsonDICT, f, ensure_ascii=False)
    return None

if __name__ == "__main__":
    txtFilePath = "./example/sample.txt"
    txt = textReadAndPrint(txtFilePath)
    print("讀取 example.txt 中的文字 ")
    print("{}\n".format(txt.split()))

    jsonDICT = {
    "name": {"zh":"", "en":""},
    "birth": {"year":"", "month":"", "date":""},
    "job": "",
    "language":[],
    "education":[],
    "spouse":""
    }
    txt = re.split(r'[\t\n ]',txt)

    jsonDICT["name"]["zh"]      = txt[1]
    jsonDICT["name"]["en"]      = txt[3] + ' ' + txt[4]
    jsonDICT["birth"]["year"]   = txt[6]
    jsonDICT["birth"]["month"]  = txt[8]
    jsonDICT["birth"]["date"]   = txt[10]
    jsonDICT["job"]             = txt[13]
    jsonDICT["language"]        = txt[15].split('、')
    jsonDICT["education"]       = txt[17].split('、')
    jsonDICT["spouse"]          = txt[19][0:3]

    #上面這個區塊，有個地方讓電腦一直做一樣的事，似乎有讓它更有效率的寫法，不知道有沒有人想到呢？

    jsonFileName = "week03_40847015S.json"
    jsonFileWriter(jsonDICT, jsonFileName)

    file = textReadAndPrint(jsonFileName)
    print("讀取 week03_40847015S.json 的內容 ")
    print(file)
