
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv(".\data\XRD_AFO.txt",sep="\t",header=None)
x = data[0]
y = data[1]
plt.figure()
plt.plot(x,y)
plt.savefig("./picture/question1.1.png",dpi=1080,bbox_inches='tight')
plt.show()