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

def enduranceplot(filename, idx, LRS, HRS):
    print(HRS)
    print(LRS)
    print(idx)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(idx,LRS, color="blue")
    ax.scatter(idx,HRS, color="red")
    ax.set_xlabel("Endurance number")
    ax.set_ylabel("Resistance [Ω]")
    ax.set_yscale('log')
    fig.savefig("result/" + filename + '.png')
    plt.close(fig)

def main():
    exd = ExData("Hf-HfOx-Hf-All.csv.json")

    dList = glob.glob('Hfdata/*')
    print(dList)

    for i, dname in enumerate(dList):
        fList = glob.glob(dname + "/*.png")
        fList_rp = [s.replace(dname + '/',' ') for s in fList]
        fList_rp2 = [f.replace('.png', '') for f in fList_rp]
        #fList_rp3 = [q.replace('40_', '40%') for q in fList_rp2]
        print(fList_rp2)
        print(os.path.split(dname)[1])

        with open('result/' + os.path.split(dname)[1] + '.csv', 'w') as csvfile:
            writer = csv.writer(csvfile, lineterminator='\n')

            HRSlist = []
            LRSlist = []
            idxlist = []

            for i, name in enumerate(fList_rp2):
                if exd.get_voltage_list(name) != None:
                    print(name)
                    #writer.writerow([name]) # フォーミング電圧を見たいとき
                    #riter.writerow(exd.get_voltage_list(name)) # フォーミング電圧を見たいとき
                    #writer.writerow(exd.get_current_list(name)) # フォーミング電圧を見たいとき

                    print([name] + exd.find_currents_by_voltage(name, 0.5) + exd.find_currents_by_voltage(name, -0.5))
                    dddd = exd.find_currents_by_voltage(name, 0.1)
                    ffff = exd.find_currents_by_voltage(name, -0.1)
                    #ON/OFF比
                    #LRS
                    #HRS
                    a = dddd[0]/dddd[1]
                    a2 = 0.1/abs(dddd[0])
                    a3 = 0.1/abs(dddd[1])

                    b = ffff[0]/ffff[1]
                    b2 = 0.1/abs(ffff[0])
                    b3 = 0.1/abs(ffff[1])
                    print([name] + [i] + dddd + [a] + [a2] + [a3])
                    print([name] + [i+1] + ffff + [b] + [b2] + [b3])
                    #名前, ON電流, OFF電流, ON/OFF比, LRS, HRS
                    writer.writerow([name] + dddd + [a] + [a2] + [a3])
                    writer.writerow([name] + ffff + [b] + [b3] + [b2])
                    LRSlist.append(a2)
                    LRSlist.append(b3)
                    HRSlist.append(a3)
                    HRSlist.append(b2)
                    idxlist.append(i*2)
                    idxlist.append(i*2+1)
            enduranceplot(os.path.split(dname)[1],idxlist,LRSlist,HRSlist)

if __name__ == "__main__":
    main()
