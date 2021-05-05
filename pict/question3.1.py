
import matplotlib.pyplot as plt
import pandas as pd
from pylab import mpl

mpl.rcParams['axes.unicode_minus'] = False
data = pd.read_csv(".\data\dos_single.csv", header=None)
x = data[0]
y = data[1]
plt.figure()
plt.plot(x,y)
plt.savefig("./picture/question3.1.png",dpi=1080,bbox_inches='tight')
plt.show()
