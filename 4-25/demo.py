# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 17:01
# @Author  : 奥利波德
# @FileName: demo.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_44265507
import pandas as pd

data = [[[1, 2, 3], [2, 3, 4], 3], [[1, 2, 3], [2, 3, 4], 3]]
with open("data.txt", 'w') as f:
    for i in data:
        f.write(str(i)+'\n')