import numpy as np

# A
A = np.array([[1, 3], [5, 7]])
detA = np.linalg.det(A)
Ainv = np.linalg.inv(A)

# B
B = np.array([[4, -6], [-8, 12]])
detB = np.linalg.det(B)
if detB != 0:
    Binv = np.linalg.inv(B)
else:
    print("B is singular and does not have an inverse.")
    Binv = None

def print_matrix(label, matrix):
    print(label)
    for row in matrix:
        print(" ".join(f"{elem:2}" for elem in row))
    print()

print(f"Determinante de A: {detA}")
print_matrix("Inversa de A:", Ainv)
print_matrix("Inversa de A:", np.linalg.inv(Ainv))

print(f"Determinante de B: {detB}")
if Binv is not None:
    print_matrix("Inversa de B:", Binv)
