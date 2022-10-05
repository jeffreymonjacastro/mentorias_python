# Bucles anidados

m = int(input("Ingrese el numero de filas: "))
n = int(input("Ingrese el numero de columnas: "))

print("El arreglo de coordenadas es:")

for i in range(1, m+1):
    for j in range(1, n+1):
        print(f"fil:{i}-col:{j}", end="   ")
    print()
