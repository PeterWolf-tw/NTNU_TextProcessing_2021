#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os, errno, json
import jieba


def text2cws(jsonFilePath: str) -> list:
    if os.path.isfile(jsonFilePath):
        with open(jsonFilePath, encoding="utf-8") as f:
            txt = f.read()
        data = json.loads(txt)
        try:
            inputSTR = data["BODY"].replace(" ", "")
            for item in ("「", "，", "、", "」", "。", '"', ",", "…", "..."):
                inputSTR = inputSTR.replace(item, "[SEP]")
            outputLIST = []
            for sentence in inputSTR.split("[SEP]"):
                outputLIST += jieba.cut(sentence)
            return outputLIST
        except Exception as e:
            raise e
    else:
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), jsonFilePath)


def termFreq(inputLIST: list) -> dict:
    result = {}
    for word in inputLIST:
        if word not in result:
            result[word] = 0
        result[word] += 1
    return result


def main():
    rootPath = "example/health/"
    words = []
    for file in os.listdir(rootPath):
        if file.endswith(".json"):
            words += text2cws(os.path.join(rootPath, file))
    print(termFreq(words))

    rootPath = "example/finance/"
    words = []
    for file in os.listdir(rootPath):
        if file.endswith(".json"):
            words += text2cws(os.path.join(rootPath, file))
    print(termFreq(words))


if _name_ == "_main_":
    main()
