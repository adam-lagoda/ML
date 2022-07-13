import torch
from matplotlib import pyplot as plt
randNum = 10000
x = torch.rand(1,randNum)
y = torch.rand(1,randNum)
x_in = torch.zeros(1,randNum)
y_in = torch.zeros(1,randNum)
exp = torch.tensor(2)
origin = torch.tensor(0)
count = torch.tensor(0)
for i in range(randNum):
    if (torch.sqrt(torch.pow((x[0,i]-origin),exp) + torch.pow((y[0,i]-origin),exp)) < 1) or (torch.sqrt(torch.
        pow((x[0,i]-origin),exp) + torch.pow((y[0,i]-origin),exp)) == 1):
        x_in[0,i] = x[0,i]
        y_in[0,i] = y[0,i]
        count += 1
ratio = count/randNum
pi = ratio*4
print(pi)
plt.plot(x,y,'b.')
plt.plot(x_in,y_in,'r.')
plt.show()