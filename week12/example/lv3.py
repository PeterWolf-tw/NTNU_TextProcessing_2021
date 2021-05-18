#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from ArticutAPI import Articut


def main(inputSTR, nlptool):


    resultDICT = articut.parse(inputSTR, level="lv3")
    return resultDICT



if __name__== "__main__":

    inputSTR = "他關上大門，把窗戶也關上了。"
    articut = Articut()
    resultLIST = main(inputSTR, articut)
    eventLIST = resultLIST["event"]
    print(eventLIST)