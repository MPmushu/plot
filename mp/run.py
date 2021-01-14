# -*- coding: utf-8 -*-
from lab.exdata import ExData

def main():
    exd = ExData("20200827.csv.json")
    print(exd)
    print(exd.get_data(" 50%AlHfOxHfSiO2-d2.5-0930_3.0_-3.0_0"))

if __name__ == "__main__":
    main()
