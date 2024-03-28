import math
from tabulate import tabulate

# Define the function
def f(x):
    return 2*math.sin(x) - x**2

# Define the derivative of the function
def df(x):
    return 2*math.cos(x) - 2*x

# Newton's method
def newton(x0):
    n = 0
    table = []

    while True:
        fx = f(x0)
        dfx = df(x0)
        x1 = x0 - fx/dfx
        delta_n = abs(x1 - x0)
        table.append([n, x0, fx, dfx, x1, delta_n, delta_n <= 0.01])

        if fx == 0 or delta_n <= 0.01:
            break

        x0 = x1
        n += 1

    print(tabulate(table, headers=["n", "x0", "f(x0)", "f'(x0)", "x1", "delta", "delta <= 0.01"], floatfmt=".10f"))
    print(f"\nLa solution est: {x1}")

# Initial value
x0 = 37/25

newton(x0)