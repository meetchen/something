# -*- coding: utf-8 -*-
# @Time    : 2021/4/21 16:51
# @Author  : 奥利波德
# @FileName: do.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_44265507
import pandas as pd

data = pd.read_csv("banklist.csv")
a = "helolo aa"
# print(a.split(" "))
# print(data.head())
# a = data['ST'].nunique()
# a = data[(data['ST']) == 'CA']
# ['Bank Name'].str.match('Bank')
# print(a['Bank' in a['Bank Name'].str])
# print(a[~a['Bank Name'].str.match('Bank')])
# print(data[(data['Acquiring Institution'])=='State Bank of Texas'])
# print(data[(data['CERT'])>20000].shape[0])
# print(data[(data['Bank Name']).str.split])
# print((data['Bank Name']).str.match("S.*"))
# print((data['Bank Name']).str.match("^s*").count())
count = 0
for item in data['Bank Name']:
    if 'Bank' not in item:
        count = count +1
print(count)
# print(data['Acquiring Institution'].value_counts()[0:5])
# print(data['Bank Name'].value_counts()[0:5])
