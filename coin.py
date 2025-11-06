import numpy as np

n = 10000
nb_head = 0

np.random.seed(2345)

for i in range(n): 
    x = np.random.binomial(1, 0.5)
    if x == 1 : 
        nb_head += 1

p_success = nb_head / n
p_success