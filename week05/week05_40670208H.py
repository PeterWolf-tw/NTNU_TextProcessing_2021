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


# inputSTR_1 = "小夫告訴大雄其實靜香喜歡的是他 " ans: {"他": ["小夫", "大雄"]}

    inputSTR_1 = "小夫告訴大雄其實靜香喜歡的是他"
    inputLIST_1 = ["小夫", "告訴", "大雄", "其實", "靜香", "喜歡", "的", "是", "他"]
    coRefDICT_1 = {inputLIST_1[8]: []}
    #"他"可能是小夫
    resultBOOL = cCommandCoRefResolver(inputLIST_1, inputLIST_1[8], inputLIST_1[0])
    if resultBOOL == True:
        coRefDICT_1[inputLIST_1[8]].append(inputLIST_1[0])
    elif resultBOOL == None:
        pass
    else:
        pass
     #"他"可能是大雄
    resultBOOL = cCommandCoRefResolver(inputLIST_1, inputLIST_1[8], inputLIST_1[2])
    if resultBOOL == True:
        coRefDICT_1[inputLIST_1[8]].append(inputLIST_1[2])
    elif resultBOOL == None:
        pass
    else:
        pass
    #"他"不會是靜香
    print(coRefDICT_1) #{"他": ["小夫", "大雄"]}
    
# inputSTR = "大雄知道靜香喜歡的是自己 "      

    inputSTR_2 = "大雄知道靜香喜歡的是自己"
    inputLIST_2 = ["大雄", "知道", "靜香", "喜歡", "的", "是", "自己"]
    coRefDICT_2 = {inputLIST_2[6]: []}
    #"自己"可能是大雄
    resultBOOL = cCommandCoRefResolver(inputLIST_2, inputLIST_2[6], inputLIST_2[0])
    if resultBOOL == True:
        coRefDICT_2[inputLIST_2[6]].append(inputLIST_2[0])
    elif resultBOOL == None:
        pass
    else:
        pass
     #"自己"可能是靜香
    resultBOOL = cCommandCoRefResolver(inputLIST_2, inputLIST_2[6], inputLIST_2[2])
    if resultBOOL == True:
        coRefDICT_2[inputLIST_2[6]].append(inputLIST_2[2])
    elif resultBOOL == None:
        pass
    else:
        pass
   
    print(coRefDICT_2) #{"自己": ["大雄", "靜香"]}  
    
    
# inputSTR = "大雄聽胖虎說靜香愛的是自己 "  

    inputSTR_3 = "大雄聽胖虎說靜香愛的是自己"
    inputLIST_3 = ["大雄", "聽", "胖虎", "說", "靜香", "愛", "的", "是", "自己"]
    coRefDICT_3 = {inputLIST_3[8]: []}
    #"自己"可能是大雄
    resultBOOL = cCommandCoRefResolver(inputLIST_3, inputLIST_3[8], inputLIST_3[0])
    if resultBOOL == True:
        coRefDICT_3[inputLIST_3[8]].append(inputLIST_3[0])
    elif resultBOOL == None:
        pass
    else:
        pass
     #"自己"可能是胖虎
    resultBOOL = cCommandCoRefResolver(inputLIST_3, inputLIST_3[8], inputLIST_3[2])
    if resultBOOL == True:
        coRefDICT_3[inputLIST_3[8]].append(inputLIST_3[2])
    elif resultBOOL == None:
        pass
    else:
        pass
    #"自己"可能是靜香
    resultBOOL = cCommandCoRefResolver(inputLIST_3, inputLIST_3[8], inputLIST_3[-5])
    if resultBOOL == True:
        coRefDICT_3[inputLIST_3[8]].append(inputLIST_3[-5])
    elif resultBOOL == None:
        pass
    else:
        pass
    
    print(coRefDICT_3)  # {"自己": ["大雄", "胖虎", "靜香"]}