#Key is a 2x1 array and cointains 2 variables for prefix and actuall key: 
# sin = [1,0], cos = [1,4], -sin = [-1,0], -cos = [-1,4]
#key just to init
def derivate(grad: int,key: list):
    n_list = []
    for i in range(0,grad):
        if key[0] == 1 and key[1] == 0:
           #np.sin(x)
           key = [1,4]
           n_list.append(0)
        elif key[0] == 1 and key[1]== 4:
            #np.cos(x)
            key = [-1,0]
            n_list.append(1)
        elif key[0] == -1 and key[1] == 0:
            #np.sin(x)
            key = [-1,4]
            n_list.append(0)
        elif key[0] == -1 and key[1] == 4:
            key =[1,0]
            n_list.append(-1)
    return n_list
   
