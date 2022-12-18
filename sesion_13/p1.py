# Recursividad
from math import pi


def PI(n):
    if n == 1:
        return 1
    else:
        return ((-1)**(n-1))/(2*n-1) + PI(n-1)


e = float(input("e: "))

n = 1
while abs(pi - 4*PI(n)) > e:
    print(f"Para n = {n} se tiene que PI({n}) es igual a: {4*PI(n)}")

    n += 1