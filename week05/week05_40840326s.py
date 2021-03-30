#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def cCommandCoRefResolver(inputLIST, coRefKeySTR, personSTR):
    "給定要做消解的字串，利用 c-command 定理濾除不可能的人名，回傳可能的指代字串"
    "[注意]：這只是極度簡化，做為初步教學說明的版本！"

    if coRefKeySTR in inputLIST:
        pass
    else:
        raise ValueError

    if personSTR in inputLIST:
        pass
    else:
        raise ValueError

    #<這段就是把 C-command 的結構考慮進去>
    personSTRIndex = inputLIST.index(personSTR)
    if inputLIST[personSTRIndex+1] == "的":
        return None
    elif inputLIST[personSTRIndex+1] == "之":
        return None
    else:
        pass
    #</這段就是把 C-command 的結構考慮進去>

    coRefKeyIndex = inputLIST.index(coRefKeySTR)
    if coRefKeyIndex > personSTRIndex:
        return True
    else:
        return False


def coRefResolver(inputLIST, coRefKeySTR, personSTR):
    "給定要做消解的字串，回傳是否可能為指代字串"
    if coRefKeySTR in inputLIST:
        pass
    else:
        raise ValueError

    if personSTR in inputLIST:
        pass
    else:
        raise ValueError

    personSTRIndex = inputLIST.index(personSTR)
    coRefKeyIndex = inputLIST.index(coRefKeySTR)
    if coRefKeyIndex > personSTRIndex:
        return True
    else:
        return False


if __name__ == "__main__":

    inputSTR = "大雄聽胖虎的妹妹說靜香愛的是自己"
    inputLIST = ["大雄", "聽", "胖虎", "的", "妹妹", "說", "靜香", "愛", "的", "是", "自己"]
    coRefDICT = {inputLIST[10]: []}
    print(inputSTR)
    resultBOOL = cCommandCoRefResolver(inputLIST, inputLIST[10], inputLIST[0])
    if resultBOOL == True:
        coRefDICT[inputLIST[10]].append(inputLIST[0])
    elif resultBOOL == None:
        pass
    else:
        pass

    resultBOOL = cCommandCoRefResolver(inputLIST, inputLIST[10], inputLIST[2])
    if resultBOOL == True:
        coRefDICT[inputLIST[10]].append(inputLIST[2])
    elif resultBOOL == None:
        pass
    else:
        pass

    resultBOOL = cCommandCoRefResolver(inputLIST, inputLIST[10], inputLIST[4])
    if resultBOOL == True:
        coRefDICT[inputLIST[10]].append(inputLIST[4])
    elif resultBOOL == None:
        pass
    else:
        pass

    resultBOOL = cCommandCoRefResolver(inputLIST, inputLIST[10], inputLIST[6])
    if resultBOOL == True:
        coRefDICT[inputLIST[10]].append(inputLIST[6])
    elif resultBOOL == None:
        pass
    else:
        pass

    print(coRefDICT) #{'自己': ['大雄', '妹妹', '靜香']}


    inputSTR_2 = "小夫告訴大雄其實靜香喜歡的是他 " #ans: {"他": ["小夫", "大雄"]}
    inputLIST_2= ["小夫","告訴","大雄","其實","靜香","喜歡","的","是","他"]
    coRefDICT_2={inputLIST_2[8]:[]}
    print(inputSTR_2)
    resultBOOL_2 = cCommandCoRefResolver(inputLIST_2, inputLIST_2[8], inputLIST_2[0])
    if resultBOOL_2 == True:
        coRefDICT_2[inputLIST_2[8]].append(inputLIST_2[0])
    elif resultBOOL_2 == None:
        pass
    else:
        pass

    resultBOOL_2 = cCommandCoRefResolver(inputLIST_2, inputLIST_2[8], inputLIST_2[2])
    if resultBOOL_2 == True:
        coRefDICT_2[inputLIST_2[8]].append(inputLIST_2[2])
    elif resultBOOL_2== None:
        pass
    else:
        pass
    print(coRefDICT_2)
    
    inputSTR_3 = "大雄知道靜香喜歡的是自己 " 
    inputLIST_3 = ["大雄", "知道", "靜香", "喜歡", "的", "是", "自己"]
    coRefDICT_3 = {inputLIST_3[6]: []}
    print(inputSTR_3)
    resultBOOL_3 = cCommandCoRefResolver(inputLIST_3, inputLIST_3[6], inputLIST_3[0])
    if resultBOOL_3 == True:
        coRefDICT_3[inputLIST_3[6]].append(inputLIST_3[0])
    elif resultBOOL_3 == None:
        pass
    else:
        pass

    resultBOOL_3 = cCommandCoRefResolver(inputLIST_3, inputLIST_3[6], inputLIST_3[2])
    if resultBOOL_3 == True:
        coRefDICT_3[inputLIST_3[6]].append(inputLIST_3[2])
    elif resultBOOL_3 == None:
        pass
    else:
        pass
    print(coRefDICT_3)

    #inputSTR = "大雄知道靜香喜歡的是自己 "      ans: {"自己": ["大雄", "靜香"]}
    #inputSTR = "大雄聽胖虎說靜香愛的是自己 "    ans: {"自己": ["大雄", "胖虎", "靜香"]}
    inputSTR_4 = "大雄聽胖虎說靜香愛的是自己 " 
    inputLIST_4 = ["大雄", "聽","胖虎","說","靜香", "愛", "的", "是", "自己"]
    coRefDICT_4 = {inputLIST_4[8]: []}
    print(inputSTR_4)
    resultBOOL_4= cCommandCoRefResolver(inputLIST_4, inputLIST_4[8], inputLIST_4[0])
    if resultBOOL_4== True:
        coRefDICT_4[inputLIST_4[8]].append(inputLIST_4[0])
    elif resultBOOL_4== None:
        pass
    else:
        pass

    resultBOOL_4 = cCommandCoRefResolver(inputLIST_4, inputLIST_4[8], inputLIST_4[2])
    if resultBOOL_4== True:
        coRefDICT_4[inputLIST_4[8]].append(inputLIST_4[2])
    elif resultBOOL_4 == None:
        pass
    else:
        pass
    resultBOOL_4 = cCommandCoRefResolver(inputLIST_4, inputLIST_4[8], inputLIST_4[4])
    if resultBOOL_4 == True:
        coRefDICT_4[inputLIST_4[8]].append(inputLIST_4[4])
    elif resultBOOL_4 == None:
        pass
    else:
        pass
    print(coRefDICT_4)
