# -*- coding: utf-8 -*-
import json


class ExData:
    # コンストラクタ
    def __init__(self, jsonFile):
        jo = open(jsonFile, 'r')
        jl = json.load(jo)
        self.data = {}
        for file in jl:
            self.data[file["filename"]] = file["data"]

    # キーの一覧を取得
    def get_key_list(self):
        return list(self.data.keys())

    # 指定したキーのデータを取得
    def get_data(self, key):
        if key not in self.data:
            return None

        return self.data[key]

    # 指定したキーの電圧を配列で取得
    def get_voltage_list(self, key):
        if key not in self.data:
            return None

        return self.data[key]["v"]

    # 指定したキーの電流を配列で取得
    def get_current_list(self, key):
        if key not in self.data:
            return None

        return self.data[key]["i"]

    # 指定したキーのi番目の電圧、電流を返す
    def get_data_body(self, key, i):
        if key not in self.data:
            return None
        if i < 0 or i >= len(self.data[key]["v"]):
            return None
        return self.data[key]["v"][i], self.data[key]["i"][i]

    # 指定したキーから特定電圧に対応する電流値を全て返す
    def find_currents_by_voltage(self, key, v):
        if key not in self.data:
            return None
        vl = self.get_voltage_list(key)
        cl = self.get_current_list(key)
        result = []
        for idx, vi in enumerate(vl):
            if vi == v:
                result.append(cl[idx])
        return result
