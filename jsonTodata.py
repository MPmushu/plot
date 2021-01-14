# -*- coding: utf-8 -*-
import csv
import os
import sys
import copy
import shutil
import glob
import pprint
import json
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import matplotlib.font_manager as fm
from matplotlib.ticker import ScalarFormatter
from matplotlib.font_manager import FontProperties
import matplotlib.ticker as mtick

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
        print(idx)
        if dv == v:
            return file["data"]["i"][idx]

def main():
    f = getCurrent("20200827.csv.json", " 20%AlHfOxHfSiO2-d0.1-A2-0827_8.0_-8.0_0", 8)
    #print(f)

if __name__ == '__main__':
    main()