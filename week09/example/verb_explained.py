#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re


from ArticutAPI import Articut

username = ""
apikey = ""
articut = Articut()

def lv1DICT(inputSTR):
    '''
    取得 lv1 的 Articut 處理結果
    '''
    global articut
    resultDICT = articut.parse(inputSTR, level="lv1")
    return resultDICT


def lv2DICT(inputSTR):
    '''
    取得 lv2 的 Articut 處理結果
    '''
    global articut
    resultDICT = articut.parse(inputSTR)
    return resultDICT


if __name__== "__main__":
    removePat1  = re.compile("<[a-zA-Z_]+>")

    inputSTR = "年輕時就創作了科學怪人這部作品"

    # 以下句法結合律說明開始
    lv1DICT = lv1DICT(inputSTR)
    lv1posSTR = ""
    for i in lv1DICT["result_pos"]:
        if len(i)==1:
            pass
        else:
            lv1posSTR = lv1posSTR + re.sub(removePat1, "", i).replace("</", "(").replace(">", ") ")
    print(lv1posSTR) #注意，lv11 會把 Verb 和 ASPECT (時態標記) 獨立切開，類比成英文就是 create-ed 視為 create / ed


    lv2DICT = lv2DICT(inputSTR)
    lv2posSTR = ""
    for i in lv2DICT["result_pos"]:
        if len(i)==1:
            pass
        else:
            lv2posSTR = lv2posSTR + re.sub(removePat1, "", i).replace("</", "(").replace(">", ") ")
    print(lv2posSTR) #注意，lv2 會把 Verb 和 ASPECT (時態標記) 結合起來，類比成英文就是 create+ed 成為 created


        # 如果只是想取出動詞的「原型」的話，可以利用 .getVerbStemLIST() 的函式操作。
    verbStemLIST = articut.getVerbStemLIST(lv1DICT)
    print(verbStemLIST)

    verbStemLIST = articut.getVerbStemLIST(lv2DICT)
    print(verbStemLIST)

    # 以上句法結合律說明結束

    # 以下利用後處理，將「了」獨立切開
    resultLIST = []
    lv1posLIST = lv1posSTR.split(" ")
    lv2posLIST = lv2posSTR.split(" ")

    for i in range(0, len(lv2posLIST)):
        if "了(VerbP)" in lv2posLIST[i]: #這裡是以「了」為例子。另一個中文的 -ed ASPECT 詞是「過」，列在下一項
            resultLIST.extend(lv2posLIST[i].replace("了(VerbP)", "(ACTION_verb) 了(VerbP)").split(" "))
        elif "過(VerbP)" in lv2posLIST[i]:
            resultLIST.extend(lv2posLIST[i].replace("過(VerbP)", "(ACTION_verb) 過(VerbP)").split(" "))
        else:
            resultLIST.append(lv2posLIST[i])

    print(resultLIST)

    # 若您最終的輸出不需要 POS 標記，只想用 $ 把字串接在一起，那麼…
    removePat2  = re.compile("\([a-zA-Z_]+\)")
    resultSTR = "$".join([re.sub(removePat2, "", i) for i in resultLIST])
    print(resultSTR)