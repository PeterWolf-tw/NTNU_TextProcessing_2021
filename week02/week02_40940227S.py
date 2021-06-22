#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def main(inputSTR):
    '''
    這支程式的主要函式(「函式」就是「功能」的意思！)
    '''
    print("Hello {}, {}".format(inputSTR, "你好"))
    StudentName = inputSTR[0:3] #用 substring 的方式取得字串中的某一部份
    StudentID = inputSTR[4:]
    print("姓名:{}".format(StudentName))
    print("學號:{}".format(StudentID))

    inputSubLIST = inputSTR.split(" ") #用 split() 函式，透過空格把字串切割成列表
    print(inputSubLIST)
    messageSTR = """
    「程式設計與基礎資料型態與中文構詞學」
    整堂課的資訊量爆炸，在知識的海洋裡衝浪
    超過癮的啊啊啊啊！
    """
    print(messageSTR)

# #字符號後，是 Python 會將之忽略的註解標記
#程式進入點！ week02.py 這支程式從這裡開始「執行」！
if __name__ == "__main__":
    nameSTR = "賴宥霖 40940227S"

    main(nameSTR)
