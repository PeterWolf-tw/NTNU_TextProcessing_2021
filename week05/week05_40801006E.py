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


# inputSTR_a = "小夫告訴大雄其實靜香喜歡的是他 " ans: {"他": ["小夫", "大雄"]}

    inputSTR_a = "小夫告訴大雄其實靜香喜歡的是他"
    inputLIST_a = ["小夫", "告訴", "大雄", "其實", "靜香", "喜歡", "的", "是", "他"]
    coRefDICT_a = {inputLIST_a[8]: []}
    #"他"可能是小夫
    resultBOOL = cCommandCoRefResolver(inputLIST_a, inputLIST_a[8], inputLIST_a[0])
    if resultBOOL == True:
        coRefDICT_a[inputLIST_a[8]].append(inputLIST_a[0])
    elif resultBOOL == None:
        pass
    else:
        pass
     #"他"可能是大雄
    resultBOOL = cCommandCoRefResolver(inputLIST_a, inputLIST_a[8], inputLIST_a[2])
    if resultBOOL == True:
        coRefDICT_a[inputLIST_a[8]].append(inputLIST_a[2])
    elif resultBOOL == None:
        pass
    else:
        pass
    #"他"不會是靜香
    print(coRefDICT_a) #{"他": ["小夫", "大雄"]}
    
# inputSTR = "大雄知道靜香喜歡的是自己 "      

    inputSTR_b = "大雄知道靜香喜歡的是自己"
    inputLIST_b = ["大雄", "知道", "靜香", "喜歡", "的", "是", "自己"]
    coRefDICT_b = {inputLIST_b[6]: []}
    #"自己"可能是大雄
    resultBOOL = cCommandCoRefResolver(inputLIST_b, inputLIST_b[6], inputLIST_b[0])
    if resultBOOL == True:
        coRefDICT_b[inputLIST_b[6]].append(inputLIST_b[0])
    elif resultBOOL == None:
        pass
    else:
        pass
     #"自己"可能是靜香
    resultBOOL = cCommandCoRefResolver(inputLIST_b, inputLIST_b[6], inputLIST_b[2])
    if resultBOOL == True:
        coRefDICT_b[inputLIST_b[6]].append(inputLIST_b[2])
    elif resultBOOL == None:
        pass
    else:
        pass
   
    print(coRefDICT_b) #{"自己": ["大雄", "靜香"]}  
    
    
# inputSTR = "大雄聽胖虎說靜香愛的是自己 "  

    inputSTR_c = "大雄聽胖虎說靜香愛的是自己"
    inputLIST_c = ["大雄", "聽", "胖虎", "說", "靜香", "愛", "的", "是", "自己"]
    coRefDICT_c = {inputLIST_c[8]: []}
    #"自己"可能是大雄
    resultBOOL = cCommandCoRefResolver(inputLIST_c, inputLIST_c[8], inputLIST_c[0])
    if resultBOOL == True:
        coRefDICT_c[inputLIST_c[8]].append(inputLIST_c[0])
    elif resultBOOL == None:
        pass
    else:
        pass
     #"自己"可能是胖虎
    resultBOOL = cCommandCoRefResolver(inputLIST_c, inputLIST_c[8], inputLIST_c[2])
    if resultBOOL == True:
        coRefDICT_c[inputLIST_c[8]].append(inputLIST_c[2])
    elif resultBOOL == None:
        pass
    else:
        pass
    #"自己"可能是靜香
    resultBOOL = cCommandCoRefResolver(inputLIST_c, inputLIST_c[8], inputLIST_c[-5])
    if resultBOOL == True:
        coRefDICT_c[inputLIST_c[8]].append(inputLIST_c[-5])
    elif resultBOOL == None:
        pass
    else:
        pass
    
    print(coRefDICT_c)  # {"自己": ["大雄", "胖虎", "靜香"]}
    

    




  