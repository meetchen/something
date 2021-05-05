# -*- coding: utf-8 -*-
# @Time    : 2020/7/18 16:37
# @Author  : 奥利波德
# @FileName: helloworld.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_44265507

import numpy as np
import matplotlib.pyplot as plt

ax = []  # 定义一个 r_y_test 轴的空列表用来接收动态的数据
ay = []  # 定义一个 r_y_test_predict 轴的空列表用来接收动态的数据
ab = []
i = 0
plt.ion()  # 开启一个画图的窗口
plt.rcParams['font.sans-serif']=['SimHei']
while True:  # 遍历0-99的值
    i = i + 1
    ax.append(i)  # 添加 i 到 r_y_test 轴的数据中
    ay.append(i ** 2)  # 添加 i 的平方到 r_y_test_predict 轴的数据中
    ab.append(i)
    plt.clf()  # 清除之前画的图
    plt.title("S2交换机-两端口实时流速图")
    plt.xlabel("time /s")
    plt.ylabel("bytes /s")
    plt.plot(ax, ay, label="S2交换机 1端口")  # 画出当前 ax 列表和 ay 列表中的值的图形
    plt.plot(ax, ab, label="S2交换机 2端口")  # 画出当前 ax 列表和 ay 列表中的值的图形
    plt.legend()
    plt.pause(0.1)  # 暂停一秒
    plt.ioff()  # 关闭画图的窗口

# plt.ion()
# plt.figure(1)
# t_list = []
# result_list = []
# t = 0
#
# while True:
#     if t >= 10 * np.pi:
#         plt.clf()
#         t = 0
#         t_list.clear()
#         result_list.clear()
#     else:
#         t += np.pi / 4
#         t_list.append(t)
#         result_list.append(np.sin(t))
#         plt.plot(t_list, result_list, c='r', ls='-', marker='o', mec='b', mfc='w')  ## 保存历史数据
#         # plt.plot(t, np.sin(t), 'o')
#         plt.pause(0.1)
