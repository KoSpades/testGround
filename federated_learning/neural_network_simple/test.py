from re import L
import torch
from model import *
from torch.utils.data import DataLoader
import time
import sys

epochs = int(sys.argv[1])  # number of rounds
data_num = int(sys.argv[2])  # batches of data >= 1

test_data = torch.load('testing/test.pt')
# train_data = torch.load('training/train0.pt')
train_data_array = []
# print(type(train_data))
for i in range(data_num):
    t = torch.load('training/train' + str(i) + '.pt')
    train_data_array.append(t)
train_data = torch.utils.data.ConcatDataset(train_data_array)

trainloader = DataLoader(train_data, batch_size=32, shuffle=True)
testloader = DataLoader(test_data, batch_size=32)

start = time.time()
net = Net()
i = train(net, trainloader, epochs=epochs)
end = time.time()
cross, acc = test(net, testloader)


print('time: {}, accuracy {}'.format(end - start, acc))
