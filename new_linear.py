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



#ynew = [dic[x[0]],dic[x[len(x)-1]]]
#xnew = [x[0],x[len(x)-1]]

xnew = sum(x)/len(x)
ynew = sum(y)/len(y)

#slope = (ynew[0]-ynew[1])/(xnew[0]-xnew[1])
#Using Least Squre Method to find Line of best fit
def slope(x,y,xnew,ynew):
    sum_xy = []
    sum_x2 = []
    for i,j in enumerate(x):
        sum_xy.append((x[i] - xnew)*(y[i]-ynew))
        sum_x2.append((x[i] - xnew)**2)
    return sum(sum_xy)/sum(sum_x2)

slope_xy = slope(x,y,xnew,ynew)
start_value = ynew - slope_xy*xnew

def grade(x):
    f = []
    for i,j in enumerate(x):
        f.append(start_value + slope_xy * x[i])
    return f

#for j in y:
#    if len(y) == len(x):
#        break 
#    else:
#        y.remove(j)
#
newf = grade(x)
for i,j in enumerate(y):
    if j > newf[i]:
        plt.vlines(x[i], newf[i], y[i],colors='r', linestyles='solid')
    else:
        plt.vlines(x[i], y[i], newf[i],colors='r', linestyles='solid')

#write this a bit prettier bruv, very ugly solution so far  


def distance(y,y_l):
    sum_len = []  
    for i,j in enumerate(y):
        sum_len.append((y[i]-y_l[i])**2)
    return sum_len

def mse(distance,x):
    return ((1/len(x)) * sum(distance))

print(mse(distance(y,newf),x))
plt.scatter(x,y)
plt.title("Linear Regression visulasitazion for Linear Dataset")
plt.plot(x,newf)
plt.savefig("assets/test_linear_mse_1.png",dpi=50)
plt.show()
plt.close()





