import numpy as np
import matplotlib.pyplot as plt

# Crear matriz de calificaciones
calificaciones = np.array([
    [7, 8, 6, 5],  # Estudiante 1
    [9, 7, 8, 6],  # Estudiante 2
    [6, 5, 9, 7],  # Estudiante 3
    [8, 6, 7, 8],  # Estudiante 4
    [5, 4, 6, 5]   # Estudiante 5
])


# Imprimir la matriz de calificaciones
print("Matriz de Calificaciones:")
print(calificaciones)
print("\n")

# Función para formatear la impresión
def imprimir_resumen(titulo, valores, etiquetas):
    print(f"{titulo}:")
    for etiqueta, valor in zip(etiquetas, valores):
        print(f"  {etiqueta}: {valor:.2f}")
    print()

# Calcular estadísticas básicas
media_asignatura = np.mean(calificaciones, axis=0)
varianza_estudiante = np.var(calificaciones, axis=1)
desviacion_total = np.std(calificaciones)

# Imprimir estadísticas básicas
imprimir_resumen("Media por asignatura", media_asignatura, ["Asignatura 1", "Asignatura 2", "Asignatura 3", "Asignatura 4"])
imprimir_resumen("Varianza por estudiante", varianza_estudiante, [f"Estudiante {i+1}" for i in range(calificaciones.shape[0])])
print(f"Desviación estándar de la matriz completa: {desviacion_total:.2f}\n")

# Obtener y ordenar valores únicos
valores_unicos = sorted(set(np.unique(calificaciones)))
print(f"Valores únicos ordenados: {valores_unicos}\n")

# Filtrar estudiantes con calificaciones mayores a 6 en todas las asignaturas
estudiantes_mayores_6 = calificaciones[np.all(calificaciones >= 6, axis=1)]
print("Estudiantes con calificaciones mayores a 6 en todas las asignaturas:")
print(estudiantes_mayores_6)
print("\n")

# Modificar matriz reemplazando calificaciones <= 6 por 10
matriz_modificada = np.where(calificaciones <= 6, 10, calificaciones)
print("Matriz modificada (calificaciones <= 6 reemplazadas por 10):")
print(matriz_modificada)
print("\n")

# Calcular estadísticas por asignatura: máximo, mínimo y mediana
max_por_asignatura = np.max(calificaciones, axis=0)
min_por_asignatura = np.min(calificaciones, axis=0)
mediana_por_asignatura = np.median(calificaciones, axis=0)

# Imprimir estadísticas por asignatura
imprimir_resumen("Máximo por asignatura", max_por_asignatura, ["Asignatura 1", "Asignatura 2", "Asignatura 3", "Asignatura 4"])
imprimir_resumen("Mínimo por asignatura", min_por_asignatura, ["Asignatura 1", "Asignatura 2", "Asignatura 3", "Asignatura 4"])
imprimir_resumen("Mediana por asignatura", mediana_por_asignatura, ["Asignatura 1", "Asignatura 2", "Asignatura 3", "Asignatura 4"])
asignaturas = ["Asignatura 1", "Asignatura 2", "Asignatura 3", "Asignatura 4"]

