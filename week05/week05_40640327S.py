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

    #a-----------------------------------------
    
    inputSTR = "小夫告訴大雄其實靜香喜歡的是他" 
    inputLIST = ["小夫", "告訴", "大雄", "其實", "靜香", "喜歡", "的", "是", "他"]
    coRefDICT = {inputLIST[8] : []}

    resultBOOL = cCommandCoRefResolver(inputLIST, inputLIST[8], inputLIST[0])
    if resultBOOL == True:
        coRefDICT[inputLIST[8]].append(inputLIST[0])
    elif resultBOOL == None:
        pass
    else:
        pass

    resultBOOL = cCommandCoRefResolver(inputLIST, inputLIST[8], inputLIST[2])
    if resultBOOL == True:
        coRefDICT[inputLIST[8]].append(inputLIST[2])
    elif resultBOOL == None:
        pass
    else:
        pass

    print(coRefDICT)

    #b------------------------------------------------

    inputSTR = "大雄知道靜香喜歡的是自己"      
    inputLIST = ["大雄", "知道", "靜香", "喜歡", "的", "是", "自己"]
    coRefDICT = {inputLIST[6] : []}

    resultBOOL = cCommandCoRefResolver(inputLIST, inputLIST[6], inputLIST[0])
    if resultBOOL == True:
        coRefDICT[inputLIST[6]].append(inputLIST[0])
    elif resultBOOL == None:
        pass
    else:
        pass

    resultBOOL = cCommandCoRefResolver(inputLIST, inputLIST[6], inputLIST[2])
    if resultBOOL == True:
        coRefDICT[inputLIST[6]].append(inputLIST[2])
    elif resultBOOL == None:
        pass
    else:
        pass

    print(coRefDICT)

    #c----------------------------------------------

    
    inputSTR = "大雄聽胖虎說靜香愛的是自己"    
    inputLIST = ["大雄", "聽", "胖虎", "說", "靜香", "愛", "的", "是", "自己"]
    coRefDICT = {inputLIST[8] : []}

    resultBOOL = cCommandCoRefResolver(inputLIST, inputLIST[8], inputLIST[0])
    if resultBOOL == True:
        coRefDICT[inputLIST[8]].append(inputLIST[0])
    elif resultBOOL == None:
        pass
    else:
        pass

    resultBOOL = cCommandCoRefResolver(inputLIST, inputLIST[8], inputLIST[2])
    if resultBOOL == True:
        coRefDICT[inputLIST[8]].append(inputLIST[2])
    elif resultBOOL == None:
        pass
    else:
        pass

    resultBOOL = cCommandCoRefResolver(inputLIST, inputLIST[8], inputLIST[4])
    if resultBOOL == True:
        coRefDICT[inputLIST[8]].append(inputLIST[4])
    elif resultBOOL == None:
        pass
    else:
        pass

    print(coRefDICT)
