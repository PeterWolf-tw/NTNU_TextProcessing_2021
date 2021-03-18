#！/ usr / bin / env python3
#-*-coding：utf-8-*-

def  main(txtFILE):
    '''
    可以通過由給定txtFILE的位置，讀取.txt純文字檔。
    '''
    with open(txtFILE, encoding = "UTF-8") as f:
        txtSTR = f.read()
    return txtSTR

if __name__ == "__main__":

    fileTUPLE = ("./example/DogPeople.txt", "./example/PeopleDog.txt")#元組裡的量不能增、減和刪
    txtSTR = main(fileTUPLE[0])                                       #取第一個值(0)

    x = txtSTR.count("婦人")                                          #計算狗咬人檔案角色出現次數
    y = txtSTR.count("土狗")                                          
    z = txtSTR.count("男")                                            
    dbpLIST = [("婦人", x), ("土狗", y), ("男", z)]                   #列表(3組)
    print(fileTUPLE[0].split("/")[1], dbpLIST)                        #先取第一個值(0)，以「斜線符號」切割後再取第二個值(1)

    resultSTR = main(fileTUPLE[1])                                    #取第二個值(1)
    xINT = resultSTR.count("婦人")                                    #計算人咬狗檔案角色出現次數
    yINT = resultSTR.count("土狗")
    zINT = resultSTR.count("男")
    pbdLIST = [("婦人", xINT), ("土狗", yINT), ("男", zINT)]          #列表(3組)
    print(fileTUPLE[1].split("/")[1], pbdLIST)                        #先取第二個值(1)，以「斜線符號」切割後再取第二個值(1)
    
    resultDICT = {"DogPeople":{"婦人":txtSTR.count("婦人"),           #左、右字典(各3個元素)
                               "土狗":txtSTR.count("土狗"),
                               "男"  :txtSTR.count("男")
                              },
                  "PeopleDog":{"婦人":resultSTR.count("婦人"),
                               "土狗":resultSTR.count("土狗"),
                               "男"  :resultSTR.count("男")
                              },
    }
    print(resultDICT)

