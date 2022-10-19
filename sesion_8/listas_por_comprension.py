# Listas por comprension
from random import randint

"""
Por extension = {1,2,3,4,5,6,7,8,9,10} // For
Por comprension = {x / 0 < x < 10} // lista por comprension

Es una forma de instrucción que permite de manera concisa la construcción de una
colección secuencial

Comprensión se basa en la notación por comprensión de conjuntos Desde la
perspectiva computacional Comprensión utiliza un estilo declarativo y funcional

List comprehension es generalmente más compacto y rápido que utilizar
estructuras de control de bucles regulares y llamadas a función para crear la lista
"""

## tipos de declaraciones de listas por comp
l = [1,1.4,True,"hello", [1,2], {"uno":1}, (5,4)]

lista1 = []

for i in range(1, 11):
    lista1.append(i)

# print(lista1)

lista2 = [i for i in range(1,11)]

# print(lista2)


# lista con condiciones
lista3 = [x for x in range(0,40,2) if x % 4 == 0 and x % 6 == 0]
# print(lista3)

s = "hola mundo"

lista4 = [z for z in range(len(s)) if s[z] in "aeiou"]
# print(lista4)

lista5 = [s[y] for y in lista4]
# print(lista5)

## lista de numeros al azar
random = [chr(randint(97, 123)) for i in range(10)]
random2 = [randint(1, 10) for i in range(10)]
# print(random)

## Crear una matriz
matriz = []

# Por extension
for i in range(3):
    fila = []

    for j in range(3):
        fila.append(j)

    matriz.append(fila)

# print(matriz)

# Por comprension
matriz2 = [[chr(97+j) for i in range(3)] for j in range(3)]

# print(matriz2)

## De matriz a lista
lista6 = [matriz2[i][j] for i in range(len(matriz2)) for j in range(len(matriz2[0]))]
# print(lista6)

## Ingresar por teclado n veces

## Por extension
# lista7_1 = []
# n_1 = int(input("N: "))
#
# for i in range(n_1):
#     num = int(input("Numero :"))
#     lista7_1.append(num)


# Por comprension
# lista7 = [int(input("Numero: ")) for i in range(int(input("N: ")))]
# print(lista7)

# Lista de palabras
string2 = "Es una forma de instrucción"


lista8 = [[i for i in s] for s in string2.split()]

# print(lista8)
# string2 = string2.split()
#
# print(string2)

## Lista de n3

lista9 = [[[x for x in range(3)] for y in range(3)] for z in range(3)]
print(lista9)
