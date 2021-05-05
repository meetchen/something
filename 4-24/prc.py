# -*- coding: utf-8 -*-
# @Time    : 2021/4/24 12:26
# @Author  : 奥利波德
# @FileName: prc.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_44265507
import pandas as pd

data = pd.read_excel("E:\Python_workspace\something\\4-24\data.xls")
mylist = []
# for row in data.iterrows():
#     # print(str(row[0]))
#     print(row[1])
#     # st = "a/"+str(row[0])+"+b-"+str(row[1])
#     # print("a//"+str(row[0])+"+b-"+str(row[1]))
#     # mylist.append("a/"+str(row[0])+"+b-"+str(row[1]))
#     # print("--------")
# # print(mylist)
# # print(data)
# print(data)
for i in range(data.shape[0]):
    print(type(data.loc[i]['r_y_test']))
    print(data.loc[i]['r_y_test'])
    string = "a/"+repr(data.loc[i]['r_y_test'])+"+b-"+repr(data.loc[i]['r_y_test_predict'])
    mylist.append(string)
    # data.loc[i]['计算值K=a/r_y_test+b-r_y_test_predict'] = string

print(mylist)
data['计算值K=a/r_y_test+b-r_y_test_predict'] = mylist
print(data)
data.to_excel("process1.xls",index=0)