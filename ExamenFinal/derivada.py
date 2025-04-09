from sympy import symbols, diff, simplify

x = symbols('x')
y = 1 / (3 - x**3 )

dy_dx = diff(y, x)
resul = simplify(dy_dx)

print(f"La derivada es {resul}")