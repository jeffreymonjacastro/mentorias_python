n = int(input("N: "))

i = 1
while i <= n:
    j = 1
    while j <= n:
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
        j += 1
    print()
    i += 1

c = input("Caracter")

i = 1
while i <= n:
    j = 1
    while j <= n:
        if i == 1 or i == n or i == j:
            print(c, end=" ")
        else:
            print(" ", end=" ")
        j += 1

    print()
    i += 1

print()

i = 1
while i <= n:
    j = 1
    while j <= n:
        if i == 1 or i == n or i + j == n + 1:
            print(c, end=" ")
        else:
            print(" ", end=" ")
        j += 1

    print()
    i += 1

c = "hello world"

for element in c:
    print(element, end="  ")

print()

for iterator in range(len(c)):
    print(c[iterator], end="  ")


n = int(input("N: "))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or i+j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

n = int(input("N: "))

for i in range(n):
    print(i, end=" ")

print()

for i in range(1, n+1):
    print(i, end=" ")

print()

for i in range(1, n+1, 2):
    print(i, end=" ")

print()

for i in range(n, -1, -1):
    print(i, end=" ")

"""RETO: Imprimir un palabra al revés"""

c = "hello world"
c_reves = ""

for i in range(len(c)-1, -1, -1):
    c_reves += c[i]

print(c)
print(c_reves)


## Funciones

c = "hello world"

def invertircadena(cadena):
    cadena_reversa = ""

    for i in range(len(cadena)-1, -1, -1):
        cadena_reversa += cadena[i]

    return cadena_reversa

print(invertircadena(c))






# print(suma(5,6))
# print(resta(5,6))
# print(multiplicacion(3,4,5))
# print()
#
# print(sumatoria(5))
# print(factorial(5))
# print()
#
# print(volumen_esfera(5))
# print()
#
# figura_triangular(5)


# Módulos
## Forma 1
import funciones

funciones.figura_triangular(5)

## Forma 2
from funciones import *

figura_triangular(5)
suma(1,2)
factorial()

## Forma 3
import funciones as rj

print(rj.volumen_esfera(5))


c = "            hello world     "

l = c.strip()

print(l)


palabra = input("Escribe: ")

lista = palabra.split()

print(lista)

print(int(lista[0]))
