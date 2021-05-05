
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv(".\data\XRD_AFO.txt", sep="\t", header=None)
x = data[0]
y = data[1]
plt.figure()
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.plot(x, y, color='green')
plt.title("X射线衍射图谱")
plt.axhline(y=0, linestyle='--', color='red')
plt.axvline(x=0, linestyle='--', color='blue')
high = y.sort_values(ascending=False)[0:5]
for i in range(5):
    plt.annotate(r"" + str(high.iloc[i]), xy=(x[high.index[i]], high.iloc[i]), xycoords='data', xytext=(+30, -30),
                 textcoords='offset points', arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.xlabel("2d")
plt.ylabel("intensity")
plt.savefig("./picture/question1.3.png", dpi=1080, bbox_inches='tight')
plt.show()
