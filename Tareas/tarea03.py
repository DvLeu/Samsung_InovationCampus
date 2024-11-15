import pandas as pd 
import numpy as np 


#? Crear un data frame de 100 x 100 con valores randoms
# Crear un DataFrame de 100x100 con valores aleatorios
df = pd.DataFrame(np.random.randint(1, 1000, size=(100, 100)), columns=[f'Col_{i+1}' for i in range(100)])
#Poner titulo a las columnas
df.index = [f"Fila_{i+1}" for i in range (100)]

#Eliminar aleatoriamente 5 datos de toda la tabla
for _ in range(5):
    i = np.random.randint(0, 100)
    j = np.random.randint(0, 100)
    df.iat[i, j] = np.nan

#Eliminar las filas con valores nulos
df = df.dropna()

#Agrupar los datos por la columna Col_1 y calcular el promedio
df_grouped = df.groupby('Col_1').mean()
print(f"Datos agrupador con promedio : \n{df_grouped}")

#Crear una nueva columna con el producto de Col_2 y Col_3
df['New_Column'] = df['Col_2'] * df['Col_3']
print(df)

#Filtrar las filas donde New_Column > 300
df_filtered = df[df['New_Column']> 300]
print(df_filtered)

df_pivot = df.pivot_table(values='New_Column', index='Col_1', aggfunc=['mean', 'sum', 'min', 'max', 'count'])
print(df_pivot)

matrix_20x20 = np.full((20, 20), 5)
print(matrix_20x20)


print(f"Imprimir tabla : \n{df}")