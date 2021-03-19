#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def readFile(txtFILE):
    '''
    藉由給定 txtFILE 的位置，讀取 .txt 純文字檔。
    '''
    with open(txtFILE, encoding="utf-8") as f:
        txtSTR = f.read()
    return txtSTR


if __name__== "__main__":
    DogPeople = "DogPeople"
    PeopleDog = "PeopleDog"
    fileTUPLE = (DogPeople, PeopleDog)
    txtSTR = readFile("./example/"+fileTUPLE[0]+".txt")

    x = txtSTR.count("婦人")
    y = txtSTR.count("土狗")
    z = txtSTR.count("男")
    dbpLIST = [("婦人", x), ("土狗", y), ("男", z)]
    print(fileTUPLE[0], dbpLIST)


    resultSTR = readFile("./example/"+fileTUPLE[1]+".txt")
    xINT = resultSTR.count("婦人")
    yINT = resultSTR.count("土狗")
    zINT = resultSTR.count("男")
    pbdLIST = [("婦人", xINT), ("土狗", yINT), ("男", zINT)]
    print(fileTUPLE[1], pbdLIST)



    #請在這一段設計你的程式，讓 resultDICT 內的 x_int, y_int, z_int 都有正確的值
    # Your Code Here
    resultDICT = {
        DogPeople:dict(item for item in dbpLIST),
        PeopleDog:dict(item for item in pbdLIST),
    }

    #答案會像
    #resultDICT = {"DogPeople":{"婦人":3,
                               #"土狗":3,
                               #"男": 4
                               #},
                  #"PeopleDog":{"婦人":3,
                               #"土狗":3,
                               #"男": 4
                               #},
    #}
    #
    print(resultDICT)
