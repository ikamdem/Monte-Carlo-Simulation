import numpy as np

x = np.random.uniform(-1,1)
print(x)

n = 100000

lst_x = []
lst_y = []

for i in range(n):
    x = np.random.uniform(-1, 1) 
    lst_x.append(x)

    y = np.random.uniform(-1, 1)
    lst_y.append(y)

nb_circle = 0
nb_square = 0

for i in range(n):
    dist_btw_mid = lst_x[i] ** 2 + lst_y[i] ** 2  
    if dist_btw_mid < 1 : 
        nb_circle += 1 
    nb_square += 1 

pi = 4 * (nb_circle / nb_square)
print(pi)