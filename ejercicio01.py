import matplotlib.pyplot as plt
import numpy as np

def funcionMatematica(x):
    return 3 * x + 1

valorX = np.linspace(-1, 1.5, 100)
valorY = funcionMatematica(valorX)

plt.plot(valorX, valorY, color="blue")


plt.scatter([-1/3, 0], [0, 1], color="black")

plt.text(-1/3, -0.3, r"$-\frac{1}{3}$", ha='center')
plt.text(0.1, 1, "1", ha='center')

plt.text(0.5, 2.5, r"$f(x) = 3x + 1$", fontsize=12)
plt.axhline(0, color="black",linewidth=0.8)
plt.axvline(0, color="black",linewidth=0.8)

plt.xlim(-0.5, 1)
plt.ylim(-0.5, 3)

plt.show()
