from re import L
import torch
from model import *
from torch.utils.data import DataLoader
import time
import numpy as np
import sys

test_data = torch.load('testing/test.pt')

result = np.zeros((40, 3))
counter = 0

for epoch in range(1, 30):
    print("epoch", epoch)
    start_time = time.time()
    train_data_array = []
    for i in range(8):
        t = torch.load('training/train' + str(i) + '.pt')
        train_data_array.append(t)
    train_data = torch.utils.data.ConcatDataset(train_data_array)

    trainloader = DataLoader(train_data, batch_size=32, shuffle=True)
    testloader = DataLoader(test_data, batch_size=32)
    net = Net()
    i = train(net, trainloader, epochs=epoch)
    end = time.time()
    cross, acc = test(net, testloader)
    time_elapsed = time.time() - start_time

    result[counter] = [epoch, time_elapsed, acc]
    counter += 1

for epoch in range(30, 301, 30):
    print("epoch", epoch)
    start_time = time.time()
    train_data_array = []
    for i in range(8):
        t = torch.load('training/train' + str(i) + '.pt')
        train_data_array.append(t)
    train_data = torch.utils.data.ConcatDataset(train_data_array)

    trainloader = DataLoader(train_data, batch_size=32, shuffle=True)
    testloader = DataLoader(test_data, batch_size=32)
    net = Net()
    i = train(net, trainloader, epochs=epoch)
    end = time.time()
    cross, acc = test(net, testloader)
    time_elapsed = time.time() - start_time

    result[counter] = [epoch, time_elapsed, acc]
    counter += 1

np.save("cifar_local.npy", result)
