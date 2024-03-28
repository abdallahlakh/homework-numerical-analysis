import math
from tabulate import tabulate

#hna kharjou g(x) mn f(x)=0 darou g(x)=x 
# Définir la fonction
def g(x):
    return math.sqrt(2*math.sin(x))

# Méthode du point fixe
def fixed_point(x0):
    n = 0
    table = []

    while True:
        # Calculer la nouvelle valeur de x
        x1 = g(x0)
        print(f"Étape {n}:")
        print(f"Calculer la nouvelle valeur de x: x1 = g(x0) = {x1}")

        # Calculer la différence entre la nouvelle valeur de x et l'ancienne
        delta_n = abs(x1 - x0)
        print(f"Calculer la différence entre la nouvelle valeur de x et l'ancienne: delta = |x1 - x0| = {delta_n}")

        table.append([n, x0, x1, delta_n, delta_n <= 0.01])

        if delta_n <= 0.01 or abs(x1) > 1e10:
            break

        print("Delta est supérieur à 0.01, donc on répète l'opération avec x0 = x1.\n")
        x0 = x1
        n += 1

    print(tabulate(table, headers=["n", "x0", "x1", "delta", "delta <= 0.01"], floatfmt=".10f"))
    print(f"\nLa solution est: {x1}")

# Valeur initiale
x0 = 37/25

fixed_point(x0)
