# Listas

L = []

for i in range(10):
    L.append(i)

print(L)

L.pop(3)

print(L)

#Slicing

print(L[-1])

print(L[4:8:2])

# Tienen una lista L y quierer printearla de der a izq o al revés

L_reves = L[::-1]

print(L_reves)

MATRICES
M = [   [1,2]  ,   [3,4]        ]

print(M[0][0] + M[1][0])

for i in range(2):
    for j in range(2):
        print(M[i][j], end=" ")
    print()

def crear_Matriz(fil, col):
    M = []

    for i in range(fil):
        fila = []

        for j in range(col):
            fila.append(0)

        M.append(fila)

    return M


def imprimir_Matrix(M):
    fil = len(M)
    col = len(M[0])

    for i in range(fil):
        for j in range(col):
            print("{:<10}".format(M[i][j]), end=" ")
        print()


# matrix = crear_Matriz(4,10)
#
# imprimir_Matrix(matrix)



paises = [ "Argentina", "Bolivia", "Brasil", "Chile", "Colombia",
"Ecuador", "Mexico", "Paraguay", "Perú", "Uruguay",
"Venezuela"]

# print(paises[8])

pbi = [[2.9, 2.5], [3.9, 4.0], [0.9, 2.2],[1.5 , 3.3],
[1.8 , 2.6], [1.0 , 2.0], [2.2, 2.3], [4.0 , 4.0],
[2.5 , 3.5], [3.0 , 3.0], [-9.5, -8.5]]

# imprimir_Matrix(pbi)

sum = 0
for i in range(len(pbi)):
    sum += pbi[i][0]

# print(sum)

datos = [ [2290, 569, 4 , 300255, 527.7, 131], [75, 22.8, 3.3, 9500, 416.7, 127],
[5.9, 1, 5.9, 744, 744, 126], [2600, 634, 4.1, 276000, 435.3, 106],
[140, 30.8, 4.5, 13430, 436, 96],[26542, 5601,4.7, 2200000, 392.8, 83],
[10900, 2964, 3.7, 869453, 293.3, 80], [11.5, 3.3, 3.5, 850, 257.6, 74],
[5.5, 1, 5.5, 386, 386, 70], [34, 7, 4.9, 2000, 287.4, 59],
[16.5, 3.6, 4.6, 965, 268.1, 58], [48, 19.6, 2.5, 2687, 137.2, 56],
[168, 31.3, 5.4, 8445, 269.6, 50], [168000, 690854, 0.2, 1308000, 1.9, 8]]

imprimir_Matrix(datos)

# Hallar el caracter relacionado con el valor de ASCII
print(chr(97))

# Encontrar el valor ASCII del caracter
print(ord("a"))


def desencriptar(horas, mensaje_encriptado):
    mensaje_desencriptado = ""




    return mensaje_desencriptado
