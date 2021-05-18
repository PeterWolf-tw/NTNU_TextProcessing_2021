import json
import nltk


def getSTR(path, name):
    with open(path, encoding="utf-8")as f:
        js = f.read()
    js = json.loads(js)
    STR = js[name]
    return STR


if __name__ == "__main__":
    jsonPath = "./foxnews.json"
    content = getSTR(jsonPath, "content")
    foxwordLIST = nltk.sent_tokenize(content)
    wordLIST = []
    for s in foxwordLIST:
        wordLIST.extend(nltk.word_tokenize(s))
    foxPOS = nltk.pos_tag(wordLIST)
    foxNER = nltk.ne_chunk(foxPOS)
    with open(jsonPath, "r+") as file:
        data = json.load(file)
        data.update(foxwordLIST)
        data.update(foxPOS)
        data.update(foxNER)
        file.seek(0)
        json.dump(data, file)
# 把 "foxnews.json" 中的 "content" 取出成為字串 foxnewsSTR
# 把 foxnewsSTR 依序斷句存成 foxsentenceLIST，寫回 foxnews.json 中；斷詞存成 foxwordLIST 寫回 foxnews.json 中；POS 處理存成 foxPOS 寫回 foxnews.json 中；NER 處理成 foxNER 寫回 foxnews.json 中。全部完成以後，請確認你的 foxnews.json 是可以被順利開啟讀取的。
