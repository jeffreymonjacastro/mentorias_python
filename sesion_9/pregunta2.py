n = int(input("Ingrese el numero de filas N:"))
m = int(input("Ingrese el numero de columnas M:"))

# Crear la matriz
# Agregar elementos a la matriz

def crearMatriz(n,m):
    matriz = []
    t = 3
    for i in range(n):
        fila = []
        for j in range(m):
            fila.append(t)
            t += 3

        matriz.append(fila)

    return matriz


# Imprimir la matriz

def imprimirMatriz(n, m, matriz):
    for i in range(n):
        for j in range(m):
            print("{:>5}".format(matriz[i][j]), end="")
        print()


matriz = crearMatriz(n,m)
imprimirMatriz(n,m,matriz)
