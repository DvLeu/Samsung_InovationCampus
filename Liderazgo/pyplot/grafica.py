import matplotlib.pyplot as plt

# Definir los periodos de neutralidad
periodos = [
    ("Primera Guerra Mundial", 1914, 1918, "Neutral"),
    ("Segunda Guerra Mundial", 1939, 1942, "Neutral"),
    ("Guerra Fría", 1947, 1991, "Neutral"),
    ("Siglo XXI", 2000, 2025, "Neutral")
]

# Crear la figura y el eje
fig, ax = plt.subplots(figsize=(15, 5))

# Dibujar los periodos de neutralidad
for periodo in periodos:
    nombre, inicio, fin, estado = periodo
    ax.barh(y=nombre, width=fin-inicio, left=inicio, color='royalblue', label=estado)

# Etiquetas y títulos
ax.set_xlabel("Año")
ax.set_title("Periodos de Neutralidad de México en el Siglo XX y XXI")
ax.set_xlim(1900, 2030)
ax.set_xticks(range(1900, 2031, 10))  # Ajuste del eje X con intervalos de 10 en 10

# Mostrar la gráfica
plt.show()
