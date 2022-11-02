from random import randint

def imprimirMatriz(matriz, n):
    for i in range(n):
        for j in range(n):
            print(matriz[i][j], end=" ")
        print()


#Validar
while True:
    n = int(input("n: "))

    if n >= 7:
        break


# Crear la matriz
matriz = []
for i in range(n):
    fila = []

    for j in range(n):
        fila.append(randint(2,9))

    matriz.append(fila)


# Imprimir la matriz
imprimirMatriz(matriz, n)

print()

# Modificar la matriz
for i in range(n):
    for j in range(n):
        if (j>i):
            matriz[i][j] = 1
        elif (i>j):
            matriz[i][j] = 0

# Imprimir la matriz
imprimirMatriz(matriz, n)


