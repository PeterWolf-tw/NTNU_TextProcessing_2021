
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
    with open(jsonFileName, mode="w" , encoding = "utf-8") as f:
        json.dump(jsonDICT, f, ensure_ascii=False)
    return None


if __name__ == "__main__":
    txtFilePath = "./example/sample.txt"
    txt = textReadAndPrint(txtFilePath)
    print("讀到原始輸入字串：{}\n\n".format(txt.split("\n")))

    jsonDICT = {
    "name": {"zh": "", "en": ""},
    "birth": {"year": "", "month": "", "date": ""},
    "job": "",
    "language": [],
    "education": [],
    "spouse": ""
    }

    line_text = txt.split("\n")

    jsonDICT["name"]["zh"] = line_text[0].split(" ")[1]
    jsonDICT["name"]["en"] = line_text[1].split(" ")[1] + line_text[1].split(" ")[2]
    jsonDICT["birth"]["year"] = line_text[2].split(" ")[1]
    jsonDICT["birth"]["month"] = line_text[2].split(" ")[3]
    jsonDICT["birth"]["date"] = line_text[2].split(" ")[5]
    jsonDICT["job"] = line_text[3].split("\t")[1]
    jsonDICT["language"] = line_text[4].split(" ")
    jsonDICT["education"] = line_text[5].split(" ")
    jsonDICT["spouse"] = line_text[6].split(" ")[1].split("（")[0]


    print(jsonDICT)

    jsonFileName = "week03_40671103h.json"

    jsonFileWriter(jsonDICT, jsonFileName)
