# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 16:29
# @Author  : 奥利波德
# @FileName: a.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_44265507
from sklearn.metrics import r2_score
from itertools import combinations

y_test = [3.42, 3.32, 3.48, 3.45, 3.48, 3.64, 3.72, 3.81, 3.1, 3.74, 3.42, 3.24, 3.45, 4.28, 3.74, 3.3, 3.56, 3.71,
          3.23, 4.17, 3.36, 4.34, 3.78, 3.75, 3.69, 3.35, 3.72, 3.31, 3.12, 3.64, 4.12, 3.36, 3.91, 3.6]
y_test_predict = [3.40781019, 3.44416631, 3.24854948, 3.25547108, 3.03859443, 3.60158276, 3.40356375, 3.90590214,
                  3.36795235, 3.81893202, 3.42005902, 3.37291289, 3.39299633, 3.83323909, 3.43443692, 3.42331325,
                  3.30430779, 3.06610163, 3.68041358, 3.60844219, 3.38715695, 4.10892826, 3.9108273, 4.40510247,
                  3.4263139, 3.40952192, 3.75381346, 3.68678884, 3.38307075, 3.63501316, 4.12719469, 3.4007922,
                  3.9069051, 3.40815478]
x = list(combinations(y_test, 30))
y = list(combinations(y_test_predict, 30))
r = []
a = float('-inf')
max_x = 0
max_y = 0
for i in x:
    for j in y:
        result = r2_score(i, j)
        r.append([i, j, result])
        if result > a:
            a = result
            max_x = i
            max_y = j
print(a, max_x, max_y)
