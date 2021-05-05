import pandas as pd
import matplotlib.pyplot as plt

plt.figure(figsize=(15, 8))
data = pd.read_excel('language_data.xlsx')
pros = list(data.groupby('Programing').groups.keys())
for pro in pros:
    item = data[data['Programing'] == pro]
    item = item.groupby('Date').sum()
    plt.plot(item.index, item['data_per'])
plt.title("TIOBE Programming Community Index")
plt.ylabel("Ratings(%)")
plt.xlabel("years(y)")
plt.grid(axis='y')
plt.legend(pros)
plt.savefig(".fig1.png", dpi=1080, bbox_inches='tight')
plt.show()
plt.cla()
# c
c = data[data['Programing'] == 'C'].groupby('Date').sum()
plt.plot(c.index, c['data_per'])
plt.title("C - TIOBE Programming Community Index")
plt.ylabel("Ratings(%)")
plt.xlabel("years(y)")
plt.grid(axis='y')
plt.savefig(".fig2.png", dpi=1080, bbox_inches='tight')
plt.show()
plt.cla()

# Python
Python = data[data['Programing'] == 'Python'].groupby('Date').sum()
plt.plot(Python.index, Python['data_per'])
plt.title("Python - TIOBE Programming Community Index")
plt.ylabel("Ratings(%)")
plt.xlabel("years(y)")
plt.grid(axis='y')
plt.savefig(".fig3.png", dpi=1080, bbox_inches='tight')
plt.show()
