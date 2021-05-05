
import matplotlib.pyplot as plt
import pandas as pd
from pylab import mpl

mpl.rcParams['axes.unicode_minus']=False
data = pd.read_csv(".\data\\band.txt", sep="\t", header=None)
x = data[0]
y = data[1]
plt.figure()
plt.rcParams['font.sans-serif'] = ['SimHei']
index = []
for i in range(x.shape[0]):
    if x[i] == 0:
        index.append(i)
for i in range(len(index)-1):
    plt.plot(x[index[i]:index[i+1]],y[index[i]:index[i+1]])
plt.plot(x[index[len(index)-1]:], y[index[len(index)-1]:])
plt.axhline(y=0, linestyle='--', color='red')
plt.title("能带曲线图谱")
plt.xlabel("k")
plt.ylabel("E(ev)")
plt.ylim(-5,5)
plt.savefig("./picture/question2.2.png", dpi=1080, bbox_inches='tight')

plt.show()
