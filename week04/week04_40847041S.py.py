#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def main(txtFILE):
    '''
    藉由給定 txtFILE 的位置，讀取 .txt 純文字檔。
    '''
    with open(txtFILE, encoding="utf-8") as f:
        txt_str = f.read()
    return txt_str


if __name__== "__main__":

    DP = "./example/DogPeople.txt"
    PD = "./example/PeopleDog.txt"
    txt_tuple = (DP, PD) #將資料放到Tuple裡，不會再更動了
    txt_str = main(txt_tuple[0])

    x = txt_str.count("婦人")
    y = txt_str.count("土狗")
    z = txt_str.count("男")
    dbpLIST = [("婦人", x), ("土狗", y), ("男", z)]
    print(txt_tuple[0].split("/")[1], dbpLIST)


    resultSTR = main(fileTUPLE[1])
    x_count = resultSTR.count("婦人")
    y_count = resultSTR.count("土狗")
    z_count = resultSTR.count("男")
    pbdLIST = [("婦人", xINT), ("土狗", yINT), ("男", zINT)]
    print(fileTUPLE[1].split("/")[1], pbdLIST)



    #請在這一段設計你的程式，讓 resultDICT 內的 x_int, y_int, z_int 都有正確的值
    # Your Code Here
    resultDICT = {"DogPeople":{"婦人":x_int=x,
                               "土狗":y_int=y,
                               "男": z_int=z
                               },
                  "PeopleDog":{"婦人":x_int=xINT,
                               "土狗":y_int=yINT,
                               "男": z_int=zINT
                               },
    }

    print(resultDICT)
