import numpy as np
import random

n = 10000
n_4 = 0

np.random.seed(2345)

for i in range(n):
    x = random.randint(1,6) 
    if x == 4 :
        n_4 += 1 

print(n_4)

p_4 = n_4 / n
print(p_4)

n_3 = 0

np.random.seed(2346)

for i in range(n):
    x = np.random.randint(1,7) 
    if x == 3 :
        n_3 += 1 

print(n_3)

p_3 = n_3 / n 
print(p_3)
