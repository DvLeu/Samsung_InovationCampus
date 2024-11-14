import numpy as np

x = np.ones((2, 3, 4))
x1 = x.shape
x2 = x.dtype
print(f"\n{x}")
print(f"{x1}\n{x2}")

b = np.ones((10,10), dtype="uint32")
b1 = b.shape
b2 = b.dtype
print(f"{b1}\n{b2}")
print(f"\n{b}")

