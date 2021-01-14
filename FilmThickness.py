# -*- coding: utf-8 -*-
import os
import glob
import xlrd


def heightEx(xlsfile):
    wb = xlrd.open_workbook(xlsfile)
    sheet = wb.sheet_by_name('フリー線分')
    return sheet.cell_value(49,11)


def main():
    l = glob.glob("./*.xls")
    FTlist = [[0 for i in range(2)] for j in range(9)]
    ds = ['d2.5', 'd1.4', 'd0.8', 'd0.6', 'd0.4', 'd0.2', 'd0.1']

    for x,name in enumerate(l):
        print(name, heightEx(name))
        FTlist[0][0] += 1
        FTlist[0][1] += heightEx(name)

        for y, d in enumerate(ds):
            if d in name:
                idx = y + 1
                break
            else:
                idx = len(ds) + 1

        FTlist[idx][0] += 1
        FTlist[idx][1] += heightEx(name)

    for z in range(9):
        if FTlist[z][0] != 0:
            print("No.", z, "ファイル数", FTlist[z][0], "合計値", FTlist[z][1], "平均値", FTlist[z][1] / FTlist[z][0])
rth;kljrntiobjrftpinhbjts

if __name__ == "__main__":
    main()

    #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa