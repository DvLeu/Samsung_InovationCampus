import numpy as np

arreglo_A = np.array([[1, -4], [-4, 1]])
arreglo_B = np.array([[1, -8], [-8, 2]])

operacion1 = arreglo_A + arreglo_B
operacion2 = arreglo_A - arreglo_B
operacion3 = 5 * arreglo_A

print(f"operacion1: \n{operacion1}")
print(f"operacion2: \n{operacion2}")
print(f"operacion3: \n{operacion3}")