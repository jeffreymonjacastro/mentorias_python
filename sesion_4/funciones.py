import funciones_secundarias as fs

def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a,b,c):
    return a*b*c


def sumatoria(n):
    sum = 0

    for i in range(1, n+1):
        sum += i

    return sum


def factorial(n):
    fact = 1

    for i in range(1, n+1):
        fact *= i

    return fact


def volumen_esfera(r):

    return (4/3)*fs.pi*(r**3)


def figura_triangular(n):
    for i in range(n):
        for j in range(n):
            if j <= i:
                print("*", end=" ")
        print()
