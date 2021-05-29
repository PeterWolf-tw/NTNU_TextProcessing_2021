
from ArticutAPI import ArticutAPI
import json

def txt2STR(path):
    with open(path, encoding="utf-8")as f:
        str = f.read()
    LIST = str.split("\n")
    return LIST
def lvl3Parse(inputSTR):
    resultDICT = articut.parse(inputSTR, level="lv3")
    return resultDICT


def json2DictReader(jsonFilePath):
    file = open(jsonFilePath, encoding="utf8")
    DICT = json.loads(file.read())
    return DICT

def writeJSON(path, data):
    with open(path, 'w', encoding="utf8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
def getEvent(LIST,CHECK):
    eventLIST = []
    for s in txtLIST:
        try:
            x = lvl3Parse(s)["event"]
        except:
            continue
        try:
            for p in x:
                if p:
                    eventLIST.append(p)
        except:
            continue
    return eventLIST


if __name__== "__main__":
    APIinfo = "account40947016S.info"
    LIST = json2DictReader(APIinfo)
    email = LIST["email"]
    API = LIST["API"]

    articut = ArticutAPI.Articut(username=email, apikey=API)
    txtPath  = "../example/text.txt"
    txtLIST = txt2STR(txtPath)
    hamsterLIST = getEvent(txtLIST,"倉鼠")

    txtPath  = "penguin.txt"
    txtLIST = txt2STR(txtPath)

    penguinLIST = getEvent(txtLIST,"皇帝企鵝")

    resultJSON = "week12_40947016S.json"
    result = {}
    result["倉鼠"] = hamsterLIST
    result["皇帝企鵝"] = penguinLIST
    writeJSON(resultJSON,result)
    

