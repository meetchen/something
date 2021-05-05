
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv(".\data\XRD_AFO.txt", sep="\t", header=None)
x = data[0]
y = data[1]
# print(data[0])
plt.figure()
plt.rcParams['font.sans-serif'] = ['SimHei']
# print(data)
plt.plot(x, y, color='green')

plt.axhline(y=0,linestyle='--',color ='red')
plt.axvline(x=0,linestyle='--',color ='blue')

plt.title("X射线衍射图谱")
plt.xlabel("2d")
plt.ylabel("intensity")
plt.savefig("./picture/question1.2.png",dpi=1080,bbox_inches='tight')
plt.show()
