# Diccionarios

"""
En Python, un diccionario es una colección de datos que, a diferencia
de otras colecciones que almacenan simples valores, permite guardar
valores similares a un mapa con la forma {llave, valor}

Las claves de un diccionario deben ser únicas y de un tipo de dato
inmutable (int, strings)
"""

a = 1
s = "a"
b = True
f = 1.4
l = []
m = [[]]

## sintaxis d = {llave:valor}
## Llaves (keys) solo pueden ser int, string
d = {"nombre":"Juan", "apellido":"Perez", "Codigo":202210514, 1:"10", 2:True, 3:[1,2,3], 4:[x for x in range(1,11)]}

print(d)

print(f"Hola {d['nombre']} {d['apellido']}")

print(d[4])

#Comandos para dict
print(list(d.keys())[0])
print(d.values())

# Modificar valores
d["nombre"] = "Romy"
print(d)

#Agregar llaves
d["key"] = False
print(d)

#Eliminar llaves
del d[1]
print(d)

#Vaciar el dict
d.clear()
print(d)

Eliminar dict
del d
print(d)



## Ejemplo 1
d_numeros = {"I":1, "V":5, "X":10, "L":50}

romanos = input("Numero romano: ")

suma = 0
for i in romanos:
    suma += d_numeros[i]

print(f"Numero: {suma}")

## Ejemplo 2

string = "hola Hola HOLA hola Hola como COMO estas you YOU U"
lista = string.split()

d = {}

for i in lista:
    d[i] = lista.count(i)

print(d)





