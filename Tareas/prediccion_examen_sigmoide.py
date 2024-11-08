import numpy as np
import matplotlib.pyplot as plt

def funcion_Sigmoide(z):
    """
    Calcula la función sigmoide para una entrada z.
    """
    return 1 / (1 + np.exp(-z))


# Inicialización de parámetros
w = 0.5  # Peso que ajusta la influencia de las horas de estudio
b = -1   # Sesgo para ajustar la posición de la función sigmoide


def prediccion(x):
    """
    Calcula la probabilidad de aprobar en función de las horas de estudio.
    """
    return funcion_Sigmoide(w * x + b)


# Datos de horas de estudio y resultados de aprobación
horas_estudio = np.array([1, 2, 3, 4, 5, 6, 7])
aprobado = np.array([0, 0, 0, 1, 1, 1, 1])

# Valores para graficar la función sigmoide
valores_x = np.linspace(0, 8, 100)
valores_y = prediccion(valores_x)

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.scatter(horas_estudio, aprobado, color="blue", label="Horas de estudio")
plt.plot(valores_x, valores_y, color="red", label="Probabilidad de aprobar")

# Líneas guía para el umbral de decisión en y = 0.5
plt.axhline(0.5, color='black', linestyle=(5, (10, 3)) , label='Umbral de decisión (0.5) ')

# Etiquetas 
plt.text(7.5, 0.25, 'Reprobará', color='blue', fontsize=12, ha='center') #Etiqueta Reprobará
plt.text(7.5, 0.75, 'Aprobará', color='green', fontsize=12, ha='center') #Etiqueta Aprobará

#Seccion donde aumentamos el eje Y en 0.1 += 0.1 ... hasta llegar a 1.0 para una mejor precision
plt.yticks(np.arange(0, 1.1, 0.1))

# Etiquetas y leyenda del gráfico
plt.xlabel('Horas de Estudio')
plt.ylabel('Probabilidad de Aprobar')
plt.title('Modelo de Predicción de Aprobación Utilizando una Función Sigmoide')
plt.legend() #Esta seccion es la legenda de la grafica si la quitamos perdemos la simbologia para saber que significa cada cosa.
plt.grid(True)
plt.show()
