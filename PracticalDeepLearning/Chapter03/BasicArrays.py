import numpy as np 

a = np.array([1, 2, 3, 4])
print(f"{a.size}\n{a.shape}\n{a.dtype}") 

b = np.array([1, 2, 3, 4], dtype="uint8")
print(f"B array : {b.dtype}")
c = np.array([1, 2, 3, 4],dtype="float64")
print(f"C array : {c.dtype}")