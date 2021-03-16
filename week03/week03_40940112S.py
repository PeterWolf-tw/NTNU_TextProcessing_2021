#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json

def textReadAndPrint(txtFILE):
    """讀入指定的純文字 txtFILE 檔案路徑，並回傳該檔案的內容。"""
    with open(txtFILE, encoding="utf-8") as f:
        txtContent = f.read()
    return txtContent

def jsonFileWriter(jsonDICT, jsonFileName):
    """轉換 jsonDICT 為 json 格式的檔案，並存檔。檔名由 jsonFileName 指定。"""
    with open(jsonFileName, mode="w", encoding="utf-8") as f:
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

    jsonDICT["name"]["zh"]      = splitTxt[0].split(" ")[1]
    jsonDICT["name"]["en"]      = " ".join(splitTxt[1].split(" ")[1:])
    jsonDICT["birth"]["year"]   = splitTxt[2].split(" ")[1]
    jsonDICT["birth"]["month"]  = splitTxt[2].split(" ")[3]
    jsonDICT["birth"]["date"]   = splitTxt[2].split(" ")[5]
    jsonDICT["job"]             = splitTxt[3].split("\t")[1]
    jsonDICT["language"]        = splitTxt[4].split(" ")
    jsonDICT["education"]       = splitTxt[5].split(" ")
    jsonDICT["spouse"]          = splitTxt[6].split(" ")[1].split("（")[0]

#     jsonDICT = {
#         "name": {
#             "zh": splitTxt[0].split(" ")[1],
#             "en": " ".join(splitTxt[1].split(" ")[1:])
#         },
#         "birth": {
#             "year": splitTxt[2].split(" ")[1],
#             "month": splitTxt[2].split(" ")[3],
#             "date": splitTxt[2].split(" ")[5]
#         },
#         "job": splitTxt[3].split("\t")[1],
#         "language": splitTxt[4].split(" "),
#         "education": splitTxt[5].split(" "),
#         "spouse": splitTxt[6].split(" ")[1].split("（")[0]
#     }

    #上面這個區塊，有個地方讓電腦一直做一樣的事，似乎有讓它更有效率的寫法，不知道有沒有人想到呢？

    jsonFileName = "week03_40940112S.json"
    jsonFileWriter(jsonDICT, jsonFileName)

    file = textReadAndPrint(jsonFileName)
    print("讀取", jsonFileName, "的內容 ")
    print(file)
