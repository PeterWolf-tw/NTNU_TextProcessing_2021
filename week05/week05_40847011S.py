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

def coRefSTR( inputLIST, coRefKeySTR, IndexL):
    coRefDICT = {coRefKeySTR: []}
    for i in IndexL:
        resultBOOL = cCommandCoRefResolver(inputLIST, coRefKeySTR, inputLIST[i])
        if resultBOOL == True:
            coRefDICT[coRefKeySTR].append(inputLIST[i])
        elif resultBOOL == None:
            pass
        else:
            pass
    return coRefDICT

if __name__ == "__main__":

    inputSTR = "大雄聽胖虎的妹妹說靜香愛的是自己"
    inputLIST = ["大雄", "聽", "胖虎", "的", "妹妹", "說", "靜香", "愛", "的", "是", "自己"]
    coRefDICT = coRefSTR( inputLIST, inputLIST[10], [0,2,4,6])
    print(inputSTR)
    print(coRefDICT,"\n") #{'自己': ['大雄', '妹妹', '靜香']}
    

    # inputSTR = "小夫告訴大雄其實靜香喜歡的是他" ans: {"他": ["小夫", "大雄"]}
    inputSTR = "小夫告訴大雄其實靜香喜歡的是他"
    inputLIST = ["小夫", "告訴", "大雄", "其實", "靜香", "喜歡", "的", "是", "他"]
    coRefDICT = coRefSTR( inputLIST, inputLIST[8], [0,2])
    print(inputSTR)
    print(coRefDICT,"\n") #{"他": ["小夫", "大雄"]}

    # inputSTR = "大雄知道靜香喜歡的是自己"      ans: {"自己": ["大雄", "靜香"]}
    inputSTR = "大雄知道靜香喜歡的是自己"
    inputLIST = ["大雄", "知道", "靜香", "喜歡", "的", "是", "自己"]
    coRefDICT = coRefSTR( inputLIST, inputLIST[6], [0,2])
    print(inputSTR)
    print(coRefDICT,"\n") #{"自己": ["大雄", "靜香"]}

    # inputSTR = "大雄聽胖虎說靜香愛的是自己"    ans: {"自己": ["大雄", "胖虎", "靜香"]}
    inputSTR = "大雄聽胖虎說靜香愛的是自己"
    inputLIST = ["大雄", "聽", "胖虎", "說", "靜香", "愛", "的", "是", "自己"]
    coRefDICT = coRefSTR( inputLIST, inputLIST[8], [0,2,4])
    print(inputSTR)
    print(coRefDICT,"\n") #{"自己": ["大雄", "胖虎", "靜香"]}
