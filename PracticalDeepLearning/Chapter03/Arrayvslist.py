import numpy as np
import time
import random

n = 100000
a = [random.random() for i in range(n)]
b = [random.random() for i in range(n)]

s = time.time()
c = [a [i] * b[i] for i in range(n)]
print (f"comprehension: {time.time()-s}")

s = time.time()
c = []

for i in range(n):
    c.append(a[i] * b[i])
print(f"for loop : {time.time()-s}")

s = time.time()
c = [0]*n
for i in range(n):
    c[i] = a[i]*b[i]
print(f"Existing list : {time.time()-s}")

x = np.array(a)
y = np.array(b)
s = time.time()
c = x * y

print(f"Numpy time : {time.time()-s}")