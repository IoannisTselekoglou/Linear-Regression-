#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import newmathlib as nmp
path_test = "/Users/jannitselekoglou/projects_Ml/mse/assets"
#name = str(input("How do  you want to save the img?\n"))


# use list comprehension cause range just takes int not float 
step_size = 0.1
x = [i*step_size for i in range(-100,100)]
y = np.sin(x)

g_x = [i for i in range(-5,5)]
g_y = g_x

fac = lambda x:np.math.factorial(x)


#Old code:
#x_test = [i*step_size for i in range(range_x,range_y)]
#T_5 = [j -1/6*(j**3) +1/120*(j**5) for j in x_test]
#T_10 = [j -1/6*(j**3) + 1/np.math.factorial(5)*(j**5) - 1/np.math.factorial(7)*(j**7) +1/np.math.factorial(9)*(j**9) for j in x_test]
#T_15 = [j -1/6*(j**3) +1/fac(5)*(j**5) -1/fac(7)*j**7 +1/fac(9)*(j**9) -1/fac(11)*(j**11) +1/fac(13)*(j**13) -1/fac(15)*(j**15) for j in x_test]0

def taylor_sin(grad: int):
    result = []
    sum_array = nmp.derivate(grad,[1,0])
    T_x = [j*0.1 for j in range(-100,100)]
    T_y_t = []
    for x in T_x:
        T_y = x
        for i in range(2,grad):
            T_y += sum_array[i]/fac(i)*x**(i)
        T_y_t.append(T_y)
    return T_x,T_y_t

T_5_x,T_5_y = taylor_sin(5)
T_15_x,T_15_y = taylor_sin(15)
T_20_x,T_20_y = taylor_sin(20)

plt.ylim([-10,10])
plt.plot(x,y,g_x,g_y,T_5_x,T_5_y,T_15_x,T_15_y,T_20_x,T_20_y)
plt.grid(True)
##plt.savefig(f"/Users/jannitselekoglou/projects_Ml/mse/assets/taylor/{name}.jpg",dpi=180)
plt.legend(["sinus","T_0","T_5","T_10","T_15"])
plt.show()

