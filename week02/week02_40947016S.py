#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def main(inputSTR):
    '''
    這支程式的主要函式(「函式」就是「功能」的意思！)
    '''
    print("Hello {}, {}".format(inputSTR, "你好"))
    inputSubSTR = inputSTR[0:11] #用 substring 的方式取得字串中的某一部份
    inputSubSTR2 = inputSTR[11:]
    print(inputSubSTR)
    print(inputSubSTR2)

    inputSubLIST = inputSTR.split(" ") #用 split() 函式，透過空格把字串切割成列表
    print(inputSubLIST[0] + " " + inputSubLIST[1])

    print(inputSubLIST[2])

# #字符號後，是 Python 會將之忽略的註解標記
#程式進入點！ week02.py 這支程式從這裡開始「執行」！
if __name__ == "__main__":
    nameSTR = "Lapor Chen 40947016S"
    main(nameSTR)
