import matplotlib.pyplot as plt
import numpy as np

x = [-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7]
y_1 = [i**3 + i**2 + i + 3 for i in x]
#calculate derivitave from y_1 function

y_2 = [1 + i**2 + 2*i for i in x]

def schnittpunkt(x_i,y_1,y_2):
    liste = {}
    for i,j in enumerate(y_1):
        if y_2[i] == y_1[i]:
            liste[x_i[i]] = y_2[i]
    return liste

#very ugly minium function for parabel eigentlich
values = schnittpunkt(x,y_1,y_2)
print(values)
dict(sorted(values.items(), key=lambda item: item[1]))
zahlx,zahly = list(values.keys()),list(values.values())


plt.plot(x,y_1,"-",x,y_2,"-")
plt.legend(["function", "derivative"])

plt.show()
