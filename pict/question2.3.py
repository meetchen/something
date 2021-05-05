
import matplotlib.pyplot as plt
import pandas as pd
from pylab import mpl

plt.figure()
mpl.rcParams['axes.unicode_minus'] = False
data = pd.read_csv(".\data\\band.txt", sep="\t", header=None)
demo = data[(data[1] > 0) & (data[1] < 5)].sort_values(by=1, ascending=True)
x1 = demo.iloc[0][0]
y1 = demo.iloc[0][1]
plt.annotate(r"bottom of conduction band", xy=(x1, y1), xycoords='data', xytext=(+0, -30),
             textcoords='offset points', arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
demo = data[(data[0] == x1) & (data[1] < 0)].sort_values(by=1, ascending=False)
x2 = demo.iloc[0][0]
y2 = demo.iloc[0][1]
plt.plot([x1, x2], [y1, y2], linestyle='--', color='black')
plt.annotate(r"top of valence band", xy=(x2, y2), xycoords='data', xytext=(+30, -30),
             textcoords='offset points', arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
x = data[0]
y = data[1]

plt.rcParams['font.sans-serif'] = ['SimHei']
index = []
for i in range(x.shape[0]):
    if x[i] == 0:
        index.append(i)
for i in range(len(index) - 1):
    plt.plot(x[index[i]:index[i + 1]], y[index[i]:index[i + 1]])
plt.plot(x[index[len(index) - 1]:], y[index[len(index) - 1]:])
plt.axhline(y=0, linestyle='--', color='red')
plt.title("能带曲线图谱")
plt.xlabel("k")
plt.ylabel("E(ev)")
y1 = input("请输入y起始值\n")
y2 = input("清输入y结束值\n")
plt.ylim(int(y1),int(y2))
plt.savefig("./picture/question2.3.png", dpi=1080, bbox_inches='tight')

plt.show()
