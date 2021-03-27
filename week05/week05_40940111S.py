#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def cCommandCoRefResolver(inputLIST, coRefKeySTR, personSTR):

    if coRefKeySTR not in inputLIST:
        raise ValueError

    if personSTR not in inputLIST:
        raise ValueError

    personSTRIndex = inputLIST.index(personSTR)
    if inputLIST[personSTRIndex+1] == "的":
        return False
    elif inputLIST[personSTRIndex+1] == "之":
        return False

    coRefKeyIndex = inputLIST.index(coRefKeySTR)
    if coRefKeyIndex > personSTRIndex:
        return True
    else:
        return False


def coRefResolver(inputLIST, coRefKeySTR, personSTR):
    if coRefKeySTR not in inputLIST:
        raise ValueError

    if personSTR not in inputLIST:
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
    else:
        pass

    resultBOOL = cCommandCoRefResolver(inputLIST, inputLIST[10], inputLIST[2])
    if resultBOOL == True:
        coRefDICT[inputLIST[10]].append(inputLIST[2])
    else:
        pass

    resultBOOL = cCommandCoRefResolver(inputLIST, inputLIST[10], inputLIST[4])
    if resultBOOL == True:
        coRefDICT[inputLIST[10]].append(inputLIST[4])
    else:
        pass

    resultBOOL = cCommandCoRefResolver(inputLIST, inputLIST[10], inputLIST[6])
    if resultBOOL == True:
        coRefDICT[inputLIST[10]].append(inputLIST[6])
    else:
        pass

    print(coRefDICT)
    
#-------------------------------------------------------------------------------------------

    inputSTR_2 = "小夫告訴大雄其實靜香喜歡的是他"
    inputLIST_2 = ["小夫", "告訴", "大雄", "其實", "靜香", "喜歡", "的", "是", "他"]
    coRefDICT_2 = {inputLIST_2[8]: []}

    #小夫：第0個，大雄：第2個，靜香：第4個；但人字旁不會是靜香
    
    #小夫=他？
    resultBOOL = cCommandCoRefResolver(inputLIST_2, inputLIST_2[8], inputLIST_2[0])
    if resultBOOL == True:
        coRefDICT_2[inputLIST_2[8]].append(inputLIST_2[0])
    else:
        pass

    #大雄=他？
    resultBOOL = cCommandCoRefResolver(inputLIST_2, inputLIST_2[8], inputLIST_2[2])
    if resultBOOL == True:
        coRefDICT_2[inputLIST_2[8]].append(inputLIST_2[2])
    else:
        pass

    print(coRefDICT_2)

#-------------------------------------------------------------------------------------------
    
    inputSTR_3 = "大雄知道靜香喜歡的是自己"
    inputLIST_3 = ["大雄", "知道", "靜香", "喜歡", "的", "是", "自己"]
    coRefDICT_3 = {inputLIST_3[6]: []}

    #大雄：第0個，靜香：第2個；自己可以是任何一位

    #大雄=自己？
    resultBOOL = cCommandCoRefResolver(inputLIST_3, inputLIST_3[6], inputLIST_3[0])
    if resultBOOL == True:
        coRefDICT_3[inputLIST_3[6]].append(inputLIST_3[0])
    else:
        pass   

    #靜香=自己？
    resultBOOL = cCommandCoRefResolver(inputLIST_3, inputLIST_3[6], inputLIST_3[2])
    if resultBOOL == True:
        coRefDICT_3[inputLIST_3[6]].append(inputLIST_3[2])
    else:
        pass     
    
    print(coRefDICT_3)

#-------------------------------------------------------------------------------------------

    inputSTR_4 = "大雄聽胖虎說靜香愛的是自己"
    inputLIST_4 = ["大雄", "聽", "胖虎", "說", "靜香", "愛", "的", "是", "自己"]
    coRefDICT_4 = {inputLIST_4[8]: []}

    #大雄：第0個，胖虎：第2個，靜香：第4個；自己可以是任何一位

    #大雄=自己？
    resultBOOL = cCommandCoRefResolver(inputLIST_4, inputLIST_4[8], inputLIST_4[0])
    if resultBOOL == True:
        coRefDICT_4[inputLIST_4[8]].append(inputLIST_4[0])
    else:
        pass   

    #胖虎=自己？
    resultBOOL = cCommandCoRefResolver(inputLIST_4, inputLIST_4[8], inputLIST_4[2])
    if resultBOOL == True:
        coRefDICT_4[inputLIST_4[8]].append(inputLIST_4[2])
    else:
        pass

    #靜香=自己？
    resultBOOL = cCommandCoRefResolver(inputLIST_4, inputLIST_4[8], inputLIST_4[4])
    if resultBOOL == True:
        coRefDICT_4[inputLIST_4[8]].append(inputLIST_4[4])
    else:
        pass

    print(coRefDICT_4)
