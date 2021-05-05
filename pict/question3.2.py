
import matplotlib.pyplot as plt
import pandas as pd
from pylab import mpl

mpl.rcParams['axes.unicode_minus'] = False
data = pd.read_csv(".\data\PDOS.csv", header=None)

plt.figure()
for i in range(data.shape[1]):
    if i % 2 == 0:
        plt.plot(data[i], data[i + 1])
plt.axvline(x=0, linestyle='--', color='blue')
plt.title("分态密度曲线图谱")
plt.xlabel("Energy(eV)")
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.ylabel("DOS")
plt.savefig("./picture/question3.2.png", dpi=1080, bbox_inches='tight')
plt.show()
