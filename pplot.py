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
import matplotlib.font_manager as fm
from matplotlib.ticker import ScalarFormatter
from matplotlib.font_manager import FontProperties
import matplotlib.ticker as mtick

# 備考
# どのOSでも使える
# 上に書いてあるライブラリ系はrequirements.txtを使ってインストールしてね
# インストールは"pip install -r requirements.txt"
# プロット時のフォントは各PCのフォントを指定してね

###############################
# 使い方
###############################

# 適当なディレクトリを用意する
# mkdir tekitouna_directory
# cd tekitouna_directory

# そのディレクトリの中にcsvファイルとpplot.pyを入れる
# ターミナル上で"python pplot.py"

# オプションも指定できる
# python pplot.py eps semilog
# のように打つ
# 対応してるのはepsとpng, linearとsemilog
# 詳しくはソースコード見て

# 勝手にプロットしてくれる

# 書式はここでも見てろhttps://qiita.com/renesisu727/items/24fc4cd8fa2635b00a0d


def addList(l): # データを辞書形式で保存
    l.append({
        "filename": "",
        "data": {
            "v": [],
            "i": []
        }
    })


def semilogGraph(filename, x, y): # セミログプロット時の書式など
    max_idx = x.index(max(x))
    min_idx = x.index(min(x))

    first = min(max_idx, min_idx)
    second = max(max_idx, min_idx)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x[first:second+1], np.abs(y[first:second+1]), color="blue")
    ax.plot(x[second:], np.abs(y[second:]), color="red")
    ax.plot(x[:first+1], np.abs(y[:first+1]), color="red")
    ax.set_xlabel("Voltage [V]")
    ax.set_ylabel("Current [A]")
    ax.set_yscale('log')

    fig.savefig(filename)
    plt.close(fig)


def linearGraph(filename, x, y): # リニアプロット時の書式など
    max_idx = x.index(max(x))
    min_idx = x.index(min(x))

    first = min(max_idx, min_idx)
    second = max(max_idx, min_idx)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x[first:second+1], y[first:second+1], color="blue")
    ax.plot(x[second:], y[second:], color="red")
    ax.plot(x[:first+1], y[:first+1], color="red")
    ax.set_xlabel("Voltage [V]")
    ax.set_ylabel("Current [A]")
    ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
    ax.ticklabel_format(style="sci",  axis="y",scilimits=(0,0))

    fig.savefig(filename)
    plt.close(fig)


def main(): # メイン関数(if文がめちゃくちゃ重なってて汚いけど許して(if文または処理に関する部分を全て関数化したい))
    # コマンドラインの引数から条件をね
    filetype = "png"
    plottype = "linear"

    if len(sys.argv) >= 2 and sys.argv[1] in ["png", "eps"]:
        filetype = sys.argv[1]

    if len(sys.argv) >= 3 and sys.argv[2] in ["linear", "semilog"]:
        plottype = sys.argv[2]


    if os.path.exists("fig/" + plottype + "/"):
        shutil.rmtree("fig/" + plottype + "/")
    os.makedirs("fig/" + plottype + "/")

    csvFile = glob.glob('./*.csv')  #ディレクト内の全てのcsvファイルを読み込む
    csvlist = []

    for name in csvFile: #ディレクトリに入っているCSVファイルを順番に読み込む
        with open(name, 'rt', newline='', encoding='utf-8') as csvfile: # CSVファイルを開く

            reader = csv.reader(csvfile)
            profile = [xxx for xxx in reader]
            count = 0
            idx = 0
            filename = ""
            addList(csvlist)
            deviceID = "Null"
            lastfilename = ""

            for line in profile[::-1]:  # CSVファイルを下から1行ずつ読み込む
                if ' TestRecord.TestTarget' in line:  # デバイスIDの処理
                    if not line[2] == ' ':  # デバイスIDが空白の時前のIDをそのまま使う
                        deviceID = line[2]

                    # ファイル名を決める
                    filename = deviceID + '_' \
                        + str(max(csvlist[idx]["data"]["v"])) + '_' \
                        + str(min(csvlist[idx]["data"]["v"]))

                    # カウントを含めないファイル名がいくつあるかカウントする
                    for namecheck in csvlist:
                        if filename in namecheck["filename"]:
                            count += 1

                    # ファイル名にカウントを付ける
                    lastfilename = filename + '_' + str(count).zfill(3)
                    count = 0

                    # 辞書にファイル名を記録する
                    csvlist[idx]["filename"] = lastfilename
                    idx += 1
                    addList(csvlist)

                elif 'DataValue' in line:  # データの処理
                    csvlist[idx]["data"]["v"].append(float(line[1]))
                    csvlist[idx]["data"]["i"].append(float(line[2]))

            # 作った辞書をjson形式で出力する
            csvlist.pop()
            path_w = name + '.json'
            with open(path_w, mode='w') as f:
                f.write(json.dumps(csvlist))

        # 辞書の中身をプロットする
        for data in csvlist:
            if plottype == "linear":
                linearGraph("fig/linear/" + data["filename"] + "." + filetype, data["data"]["v"], data["data"]["i"])
            else:
                semilogGraph("fig/semilog/" + data["filename"] + "." + filetype, data["data"]["v"], data["data"]["i"])

        csvlist.clear()

# おまじないみたいなもん
if __name__ == "__main__":
    main()