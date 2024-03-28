import math
from tabulate import tabulate

# Define the function
def f(x):
    return 2*math.sin(x) - x**2

# Bisection method
def bisection(a, b):
    n = 0
    delta_initial = abs(b - a)
    table = []

    while True:
        x = (a + b) / 2
        fx = f(x)
        fa = f(a)
        fb = f(b)
        delta_n = delta_initial / 2**(n+1)
        table.append([n, a, b, x, fa, fb, fx, delta_n, delta_n <= 0.01])

        if fx == 0 or delta_n <= 0.01:
            break
        elif fa * fx < 0:
            b = x
        else:
            a = x

        n += 1

    print(tabulate(table, headers=["n", "a", "b", "x", "f(a)", "f(b)", "f(x)", "delta", "delta <= 0.01"], floatfmt=".10f"))
    print(f"\nThe solution is: {x}")

# Initial values
a = 1
b = 3/2

bisection(a, b)