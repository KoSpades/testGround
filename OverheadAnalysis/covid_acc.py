import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("acc.txt").iloc[:, 1]

acc_arr = []
for i in range(len(df)):
    cur_val = float(df[i][10:])
    acc_arr.append(cur_val)

plt.plot(acc_arr)
plt.show()


