# Archivos

inventario = open("inventario.txt", "r")

precio = open("precios.txt", "r")

empresa = open("empresa.txt", "w")

p_inv = inventario.readlines()
p_pre = precio.readlines()

# De un archivo a una matriz
p_inv2 = []
for i in p_inv:
    p_inv2.append(i[:len(i)-1].split(","))

p_pre2 = []
for i in p_pre:
    p_pre2.append(i[:len(i)-1].split(","))


matriz = []
for i in range(len(p_inv2)):
    fila = []

    for j in range(len(p_inv2[0])):
        fila.append(p_inv2[i][j])

        if p_pre2[i][j] not in matriz:
            fila.append(p_pre2[i][j])

    matriz.append(fila)

# Escribir de Matriz a un archivo
for i in range(len(matriz)):
    datos = []

    for j in range(len(matriz[0])):
        datos.append(str(matriz[i][j]))

    cadena = ",".join(datos)

    empresa.write(cadena + "\n")

empresa.close()