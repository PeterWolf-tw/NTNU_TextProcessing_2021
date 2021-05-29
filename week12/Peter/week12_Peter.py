import json
from ArticutAPI import Articut


def txtReader(jsonFilePath):
    with open(jsonFilePath, encoding="utf-8") as f:
        Content = f.read()
    return Content


def jsonFileWriter(jsonDICT, jsonFileName):
    with open(jsonFileName, mode="w") as f:
        json.dump(jsonDICT, f, ensure_ascii=False)
    return None


if __name__ == "__main__":
    articut = Articut(
        username="laporisbraindead@gmail.com", apikey="1fawHVpX6VJJN=W5gImYKzS+q623Lup"
    )
    MouseSTR = txtReader("../example/text.txt")

    MouseDICT = articut.parse(MouseSTR, level="lv3")
    MouseLIST = MouseDICT["event"]
    print(MouseLIST)

    PenguinSTR = txtReader("penguin.txt")

    PenguinDICT = articut.parse(PenguinSTR, level="lv3")
    PenguinLIST = PenguinDICT["event"]
    print(PenguinLIST)

    ResultDICT = {"倉鼠": [], "皇帝企鵝": []}
    for item in MouseLIST:
        if item != "\n" and item != []:
            ResultDICT["倉鼠"].append(item)
    for item in PenguinLIST:
        if item != "\n" and item != []:
            ResultDICT["皇帝企鵝"].append(item)
    jsonFileWriter(ResultDICT, "week12_Peter.json")
