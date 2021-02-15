# -*- coding: utf-8 -*-
from lab.exdata import ExData
import csv
import os
import sys
import glob
import shutil
import glob
import pprint
import json
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm
from matplotlib.ticker import ScalarFormatter
from matplotlib.font_manager import FontProperties
import matplotlib.ticker as mtick


def main():
    exd = ExData("Hf-HfOx-Hf-All.csv.json")

    dList = glob.glob('HfForming/*')
    print(dList)

    for i, dname in enumerate(dList):
        fList = glob.glob(dname + "/*.png")
        fList_rp = [s.replace(dname + '/',' ') for s in fList]
        fList_rp2 = [f.replace('.png', '') for f in fList_rp]
        print(fList_rp2)
        print(os.path.split(dname)[1])

        with open(os.path.split(dname)[1] + '.csv', 'w') as csvfile:
            writer = csv.writer(csvfile, lineterminator='\n')

            HRSlist = []
            LRSlist = []
            idxlist = []

            for i, name in enumerate(fList_rp2):
                if exd.get_voltage_list(name) != None:
                    print(name)
                    writer.writerow([name])
                    writer.writerow(exd.get_voltage_list(name))
                    writer.writerow(exd.get_current_list(name))

if __name__ == "__main__":
    main()
