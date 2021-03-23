#!/usr/bin/env python3
# -*- coding:utf-8 -*- 加了這一行才能確保編碼也能讀出中文

def cCommandCoRefResolver(inputLIST, coRefKeySTR, personSTR):
    "給定要做消解的字串，利用 c-command 定理濾除不可能的人名，回傳可能的指代字串"
    "[注意]：這只是極度簡化，做為初步教學說明的版本！"
    if coRefKeySTR in inputLIST:#該指代是否在字串內
        pass
    else:
        raise ValueError
    if personSTR in inputLIST:#某人名是否在字串內
        pass
    else:
        raise ValueError

    #<這段就是把 C-command 的結構考慮進去>
    personSTRIndex = inputLIST.index(personSTR)
    if inputLIST[personSTRIndex+1] == "的":#此人名在句法樹中是否為單節點轉折
        return None
    elif inputLIST[personSTRIndex+1] == "之":
        return None
    else:
        pass
    coRefKeyIndex = inputLIST.index(coRefKeySTR)
    if coRefKeyIndex > personSTRIndex:
        return True
    else:
        return False
    
#因功能相似，又程式碼中沒有執行到，故作業省略def coRefResolver(inputLIST, coRefKeySTR, personSTR):



if __name__ == "__main__":
   
    inputSTR = "大雄聽胖虎的妹妹說靜香愛的是自己"
    inputLIST = ["大雄", "聽", "胖虎", "的", "妹妹", "說", "靜香", "愛", "的", "是", "自己"]
    coRefDICT = {inputLIST[10]: []}
    #「自己」是否可能是「大雄」
    resultBOOL = cCommandCoRefResolver(inputLIST, inputLIST[10], inputLIST[0])
    if resultBOOL == True:
        coRefDICT[inputLIST[10]].append(inputLIST[0])
    elif resultBOOL == None:
        pass
    else:
        pass
    #「自己」是否可能是「胖虎」
    resultBOOL = cCommandCoRefResolver(inputLIST, inputLIST[10], inputLIST[2])
    if resultBOOL == True:
        coRefDICT[inputLIST[10]].append(inputLIST[2])
    elif resultBOOL == None:
        pass
    else:
        pass
    #「自己」是否可能是「妹妹」
    resultBOOL = cCommandCoRefResolver(inputLIST, inputLIST[10], inputLIST[4])
    if resultBOOL == True:
        coRefDICT[inputLIST[10]].append(inputLIST[4])
    elif resultBOOL == None:
        pass
    else:
        pass
    #「自己」是否可能是「靜香」
    resultBOOL = cCommandCoRefResolver(inputLIST, inputLIST[10], inputLIST[6])
    if resultBOOL == True:
        coRefDICT[inputLIST[10]].append(inputLIST[6])
    elif resultBOOL == None:
        pass
    else:
        pass

    print(coRefDICT) #{'自己': ['大雄', '妹妹', '靜香']}




    inputSTR_2 = "小夫告訴大雄其實靜香喜歡的是他"
    inputLIST_2 = ["小夫", "告訴", "大雄", "其實", "靜香", "喜歡", "的", "是", "他"]
    coRefDICT_2 = {inputLIST_2[8]: []}
    #「他」是否可能是「小夫」
    resultBOOL = cCommandCoRefResolver(inputLIST_2, inputLIST_2[8], inputLIST_2[0])
    if resultBOOL == True:
        coRefDICT_2[inputLIST_2[8]].append(inputLIST_2[0])
    elif resultBOOL == None:
        pass
    else:
        pass
    #「他」是否可能是「大雄」
    resultBOOL = cCommandCoRefResolver(inputLIST_2, inputLIST_2[8], inputLIST_2[2])
    if resultBOOL == True:
        coRefDICT_2[inputLIST_2[8]].append(inputLIST_2[2])
    elif resultBOOL == None:
        pass
    else:
        pass
    #他的部首是人部，所以不會是靜香
    print(coRefDICT_2) #{"他": ["小夫", "大雄"]}



    inputSTR_3 = "大雄知道靜香喜歡的是自己"
    inputLIST_3 = ["大雄", "知道", "靜香", "喜歡", "的", "是", "自己"]
    coRefDICT_3 = {inputLIST_3[6]: []}
    #「自己」是否可能是「大雄」
    resultBOOL = cCommandCoRefResolver(inputLIST_3, inputLIST_3[6], inputLIST_3[0])
    if resultBOOL == True:
        coRefDICT_3[inputLIST_3[6]].append(inputLIST_3[0])
    elif resultBOOL == None:
        pass
    else:
        pass
    #「自己」是否可能是「靜香」
    resultBOOL = cCommandCoRefResolver(inputLIST_3, inputLIST_3[6], inputLIST_3[2])
    if resultBOOL == True:
        coRefDICT_3[inputLIST_3[6]].append(inputLIST_3[2])
    elif resultBOOL == None:
        pass
    else:
        pass
    
    print(coRefDICT_3) #{"自己": ["大雄", "靜香"]}   
    
    
    
    inputSTR_4 = "大雄聽胖虎說靜香愛的是自己"
    inputLIST_4 = ["大雄", "聽", "胖虎", "說", "靜香", "愛", "的", "是", "自己"]
    coRefDICT_4 = {inputLIST_4[8]: []}
    #「自己」是否可能是「大雄」
    resultBOOL = cCommandCoRefResolver(inputLIST_4, inputLIST_4[8], inputLIST_4[0])
    if resultBOOL == True:
        coRefDICT_4[inputLIST_4[8]].append(inputLIST_4[0])
    elif resultBOOL == None:
        pass
    else:
        pass
    #「自己」是否可能是「胖虎」
    resultBOOL = cCommandCoRefResolver(inputLIST_4, inputLIST_4[8], inputLIST_4[2])
    if resultBOOL == True:
        coRefDICT_4[inputLIST_4[8]].append(inputLIST_4[2])
    elif resultBOOL == None:
        pass
    else:
        pass
    #「自己」是否可能是「靜香」
    resultBOOL = cCommandCoRefResolver(inputLIST_4, inputLIST_4[8], inputLIST_4[4])
    if resultBOOL == True:
        coRefDICT_4[inputLIST_4[8]].append(inputLIST_4[4])
    elif resultBOOL == None:
        pass
    else:
        pass

    print(coRefDICT_4) #{"自己": ["大雄", "胖虎", "靜香"]} 
    