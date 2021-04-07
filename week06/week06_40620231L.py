#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#讀取 json 的程式
import json
def jsonReader(jsonFILE):
    with open(jsonFILE, encoding="utf-8") as f:#將讀入的json檔案以純文字載入並回傳
        txtDICT = json.loads(f.read())
    return txtDICT

#將字串轉為「句子」列表的程式
def sentence2LIST_v1(inputSTR):
    for item in ( "、", "，","。", ","):
        inputSTR = inputSTR.replace(item, "<MyCuttingMark>")
        
    inputSTR = inputSTR.replace("…", "")
    inputSTR = inputSTR.replace("...", "")
    if "2<MyCuttingMark>718" in inputSTR:
        inputSTR = inputSTR.replace("2<MyCuttingMark>718", "2,718")
    #inputSTR = inputSTR.strip("<MyCuttingMark>")#適用於字串，以清除結尾不要的東西
    resultLIST = inputSTR.split("<MyCuttingMark>")
    #return resultLIST
    return resultLIST[:-1]#作用同上，從後面扣回去。
if __name__== "__main__":
    fileTUPLE = ("./example/news.json", "./example/test.json") 
    jsonDICT = jsonReader(fileTUPLE[0])
    testJsonDICT = jsonReader(fileTUPLE[1])    
    news_LIST = sentence2LIST_v1(jsonDICT["text"])
    test_LIST = testJsonDICT["sentence"]
    print(news_LIST)
    print(test_LIST)
    #設定要讀取的 news.json 路徑

    #將 news.json 利用 [讀取 json] 的程式打開

    #將讀出來的內容字串傳給 [將字串轉為「句子」 列表」]的程式，存為 newsLIST

    #設定要讀取的 test.json 路徑

    #將 test.json 的 sentenceLIST 內容讀出，存為 testLIS

    #測試是否達到作業需求
    if news_LIST == test_LIST:
        print("作業過關！")
    else:
        print("作業不過關，請回到上面修改或是貼文求助！")