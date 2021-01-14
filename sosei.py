# -*- coding: utf-8 -*-
import json

import numpy as np
from scipy import signal

# 指定したファイル名のデータを返す
def getFile(jsonfile, filename):
    jo = open(jsonfile, 'r')
    jl = json.load(jo)
    for file in jl:
        if file["filename"] == filename:
            return file
    return None

# 指定したファイル名・電圧に対応する最初の電流値を返す
def getCurrent(jsonfile, filename, v):
    file = getFile(jsonfile, filename)
    for idx, dv in file["data"]["v"]:
        if dv == v:
            return file["data"]["i"][idx]

# 最大ピークの配列を返す
def getMaxPeaks(jsonfile, filename, order):
    file = getFile(jsonfile, filename)
    i = np.array(file["data"]["i"])
    return signal.argrelmax(i, order=order)

# 最小ピークの配列を返す
def getMinPeaks(jsonfile, filename, order):
    file = getFile(jsonfile, filename)
    i = np.array(file["data"]["i"])
    return signal.argrelmin(i, order=order)

def main():
    f = getFile("20200827.csv.json", " 30%AlHfOxHfSiO2-d0.8-B2-0813_2.5_-2.5_4")
    maxpeaks = getMaxPeaks("20200827.csv.json", " 30%AlHfOxHfSiO2-d0.8-B2-0813_2.5_-2.5_4", 5)
    print("最大ピーク:")
    for p in maxpeaks[0]:
        print("(", f["data"]["v"][int(p)], ",", f["data"]["i"][int(p)], ")")

    minpeaks = getMinPeaks("20200827.csv.json", " 30%AlHfOxHfSiO2-d0.8-B2-0813_2.5_-2.5_4", 5)
    print("最小ピーク:")
    for p in minpeaks[0]:
        print("(", f["data"]["v"][int(p)], ",", f["data"]["i"][int(p)], ")")

if __name__ == '__main__':
    main()