# Selectivas y repetitivas

# n = int(input("Ingrese la cantidad de objetos a clasificar: "))
#
# while n < 3 or n > 20:
#     n = int(input("Ingrese la cantidad de objetos a clasificar: "))


# Validación
while True:
    n = int(input("Ingrese la cantidad de objetos a clasificar: "))

    if 3 < n < 20:
        break

# Contadores
peligroso = 0
cercano = 0
alejado = 0

# Operaciones
i = 1
while i <= n:
    print("Coordenadas del objeto")

    x = int(input("Ingrese la coordenada x: "))
    y = int(input("Ingrese la coordenada y: "))

    distancia = (x**2 + y**2)**0.5

    if distancia < 2:
        peligroso += 1
    elif 2 <= distancia < 20:
        cercano += 1
    else:
        alejado += 1

    i += 1

# Output

print("Reporte")
print(f"Se tiene {peligroso} objetos peligrosos")
print(f"Se tiene {cercano} objetos cercanos")
print(f"Se tiene {alejado} objetos alejados")