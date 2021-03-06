import matplotlib.pyplot as plt
import numpy as np
import random
from scipy import interpolate 
from sklearn.metrics import mean_squared_error
var = 20

#x = [random.randrange(1,var,2) for i in range(var)]
#y = [2 + 2*x[i] + random.randrange(1,var,2) for i in range(var)]

#create rnd linear dataset
x = np.arange(var)
delta = np.random.uniform(-10,10,size=(var,))
y = 4 + x*3 + delta

dic = {}

for i,j in enumerate(x):
    dic[j] = y[i]

#problem: because the numbers are generated randomly, there a multiple x values with different y values.. how should i fix this shit

plt.scatter(x,y)

ynew = [dic[x[0]],dic[x[len(x)-1]]]
xnew = [x[0],x[len(x)-1]]

#x_1,y_1 = plt.plot(xnew,ynew,1)
#x_1_t = x_1.get_xdata()
#x_plot_1,x_plot_2 = dic[x_1_t[0]], dic[x_1_t[1]]
#steigung = (x_plot_2 - x_plot_1)/(x_1_t[1]-x_1_t[0])

steigung = (ynew[0]-ynew[1])/(xnew[0]-xnew[1])

f = []
add = 3
for i,j in enumerate(x):
    f.append(add + dic[x[0]] + steigung * x[i])

for j in y:
    if len(y) == len(x):
        break 
    else:
        y.remove(j)

for i,j in enumerate(y):
    if j > f[i]:
        plt.vlines(x[i], f[i], y[i],colors='r', linestyles='solid')
    else:
        plt.vlines(x[i], y[i], f[i],colors='r', linestyles='solid')

#write this a bit prettier bruv, very ugly solution so far  


def distance(y,y_l):
    sum_len = []  
    for i,j in enumerate(y):
        sum_len.append((y[i]-y_l[i])**2)
    return sum_len

def mse(distance,x):
    return ((1/len(x)) * sum(distance))


plt.title("Linear Regression visulasitazion for Linear Dataset")
plt.plot(x,f,"-")
plt.savefig("assets/test_linear_mse.png")
plt.show()
plt.close()





