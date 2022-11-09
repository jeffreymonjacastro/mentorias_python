# Si está en modo "r" (solo lectura) y el archivo no existe, saldrá error
inputfile = open("hola.txt", "r")

inputfile = open("disket.txt", "r")

cadena = ""
for i in inputfile:
    cadena += i
print(cadena)


cadena = inputfile.readlines()
print(cadena)

nueva_lista = []

for i in cadena:
    nueva_lista.append(i[:len(i)-1])

print(nueva_lista)

nueva_lista2 = []

for i in nueva_lista:
    nueva_lista2.append(i.split(","))

print(nueva_lista2)

for i in range(len(nueva_lista2)):
    for j in range(len(nueva_lista2[0])):
        print(nueva_lista2[i][j], end=" ")
    print()



# Edita el archivoo

Editar archivos
inputfiles = open("disket.txt", "w+")
inputfiles.write("HELLOO\n")
inputfiles.write("Moon a")
inputfiles.close()

# Agregar texto al archivoo
inputfiles = open("disket.txt", "a")
inputfiles.write("Fabri,bio\n")
inputfiles.close()


inputfile = open("disket.txt", "r")

lista = inputfile.readlines()

lista2 = []
for i in lista:
    lista2.append(i[:len(i)-1])

lista3 = []
for i in lista2:
    lista3.append(i.split(","))

for i in range(len(lista3)):
    for j in range(len(lista3[0])):
        print(lista3[i][j], end=" ")
    print()

for i in range(1, len(lista3)):
    print(lista3[i][0])
