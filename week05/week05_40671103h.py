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

def coRef_answer(inputSTR,inputLIST,target,maybe):
    coRefDICT = {inputLIST[target]: []}
    for i in maybe:
        resultBOOL = cCommandCoRefResolver(inputLIST, inputLIST[target], inputLIST[i])
        if resultBOOL == True:
            coRefDICT[inputLIST[target]].append(inputLIST[i])
        elif resultBOOL == None:
            pass
        else:
            pass


    return coRefDICT


if __name__ == "__main__":


    inputSTR = [
     "大雄聽胖虎的妹妹說靜香愛的是自己"
    ,"小夫告訴大雄其實靜香喜歡的是他 "
    ,"大雄知道靜香喜歡的是自己 "
    ,"大雄聽胖虎說靜香愛的是自己 "]

    inputLIST = [
    ["大雄", "聽", "胖虎", "的", "妹妹", "說", "靜香", "愛", "的", "是", "自己"],
    ["小夫","告訴","大雄","其實","靜香","喜歡","的","是","他"],
    ["大雄","知道","靜香","喜歡","的","是","自己"],
    ["大雄","聽","胖虎","說","靜香","愛","的","是","自己"]]

    print(coRef_answer(inputSTR[0],inputLIST[0],10,[0,2,4,6]))

    print(coRef_answer(inputSTR[1],inputLIST[1],8,[0,2]))

    print(coRef_answer(inputSTR[2],inputLIST[2],6,[0,2]))

    print(coRef_answer(inputSTR[3],inputLIST[3],8,[0,2,4]))




