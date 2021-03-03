#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def main(inputSTR):
    
    myNameSTR = inputSTR[0:7] 
    myIdSTR = inputSTR[8:17]
    myInfoSTR = myNameSTR + " " + myIdSTR
    
    print(myInfoSTR)
    
    inputLIST = inputSTR.split(" ")
    
    print(inputLIST)
    print("私の名前：{}".format(inputLIST[0]))
    print("私の学籍番号：{}".format(inputLIST[1]))
    
if __name__ == "__main__":
    nameSTR= "林·イーノック 40992022M"
    
    main(nameSTR)
