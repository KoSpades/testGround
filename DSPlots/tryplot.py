from matplotlib import pyplot as plt
import numpy as np


# FL data

fl_acc = []
fl_time = []

with open("DSPlots/federated_acc.txt") as f:
    for line in f:
        fl_acc.append(float(line.split(":")[-1]))

with open("DSPlots/federated_time.txt") as f:
    for line in f:
        fl_time.append(float(line.split(":")[-1]))

for i in range(1, 300):
    fl_time[i] = fl_time[i] - fl_time[0]

fl_time[0] = 0

# Local data
local_data = np.load("DSPlots/cifar_local.npy")
print(local_data)

# plt.plot(fl_time, fl_acc)
# plt.show()
