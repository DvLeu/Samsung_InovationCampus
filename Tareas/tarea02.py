import numpy as np 

#Crear matriz de calificaciones
calificaciones = np.array([
    [7,8,6,5],
    [9,7,8,6],
    [6,5,9,7],
    [8,6,7,8],
    [5,4,6,5]
])
#Imprimir la matriz de califaciones
print(f"Matriz de calificaciones : \n{calificaciones}")

#Calcular estadisticas basicas :
media_asignatura = np.mean(calificaciones, axis=0)
print(f"Media por asignatura : \n{media_asignatura}")

#Varianza por estudiante 
varianza_estudiante = np.var(calificaciones, axis=1)
print(f"Varianza por estudiante : \n{varianza_estudiante}")

#Desviacion estandar de la matriz completa : 
desviacion_total = np.std(calificaciones)
print(f"Desviacion estandar de la matriz completa : \n{desviacion_total}")

#Obtener los valores unicos y ordenarlos 
valores_unicos = np.unique(calificaciones)
valores_unicos_ordenados = sorted(set(valores_unicos))
print(f"\nValores unicos ordenados : \n{valores_unicos_ordenados}")


#Comienza codigo con los filtrados por calificaciones

#Filtrar estudiantes con calificaciones mayores a 6 
estudiantes_mayores_6 = calificaciones[np.all(calificaciones >= 6, axis=1)]
print(f"Estudiantes con calificaciones mayores a 6 en todas las asignaturas :\n {estudiantes_mayores_6}")

# Modificar la matriz reemplazando valores menores o iguales a 6 por 10
matriz_modificada = np.where(calificaciones <= 6, 10, calificaciones)
print(f"Matriz remplazado donde calificaciones menores o iguales a 6 cambian a 10 : {matriz_modificada}")


# Calcular estadísticas por asignatura
# Máximo, mínimo y mediana por asignatura
max_por_asignatura = np.max(calificaciones, axis=0)
min_por_asignatura = np.min(calificaciones, axis=0)
mediana_por_asignatura = np.median(calificaciones, axis=0)

print("\nMáximo por asignatura:", max_por_asignatura)
print("Mínimo por asignatura:", min_por_asignatura)
print("Mediana por asignatura:", mediana_por_asignatura)

# Crear un resumen completo
print("\nResumen completo por asignatura:")
for i in range(calificaciones.shape[1]):
    print(f"Asginatura {i+1}:")
    print("  Media:", media_asignatura[i])
    print("  Máximo:", max_por_asignatura[i])
    print("  Mínimo:", min_por_asignatura[i])
    print("  Mediana:", mediana_por_asignatura[i])
    print("  Valores únicos:", np.unique(calificaciones[:, i]))
    print()