#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import nltk, json

if __name__ == "__main__":
    with open("example/foxnews.json", "r", encoding="utf-8") as f:
        data = json.loads(f.read())
    foxnewsSTR = data["content"]
    foxsentenceLIST = nltk.sent_tokenize(foxnewsSTR)
    data["foxsentenceLIST"] = foxsentenceLIST
    foxwordLIST = []
    for sentence in foxsentenceLIST:
        foxwordLIST += nltk.word_tokenize(sentence)
    data["foxwordLIST"] = foxwordLIST
    foxPOS = nltk.pos_tag(foxwordLIST)
    data["foxPOS"] = foxPOS
    foxNER = nltk.ne_chunk(foxPOS)
    data["foxNER"] = foxNER
    print(foxNER)
    with open("example/foxnews.json", "w", encoding="utf-8") as f:
        json.dump(data, f)

    foxnewsSTR = foxnewsSTR.replace("White House", "white house")
    foxsentenceLIST = nltk.sent_tokenize(foxnewsSTR)
    foxwordLIST = []
    for sentence in foxsentenceLIST:
        foxwordLIST += nltk.word_tokenize(sentence)
    foxPOS = nltk.pos_tag(foxwordLIST)
    foxNER = nltk.ne_chunk(foxPOS)
    print(foxNER)
