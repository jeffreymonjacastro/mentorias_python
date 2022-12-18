# Linear Search

from random import randint

##### Para crear una lista aleatoria
def listaAleatoria(n):
    l = []

    for i in range(n):
        l.append(randint(1, 1000))

    return l

lista_aleatoria = listaAleatoria(100)

e = 16
# print(lista_aleatoria)

### Búsqueda Lineal
# PC4
# editar el algoritmo de linear search

def linearSearch(lista, element):
    for i in range(len(lista)):
        if element == lista[i]:
            return True
        else:
            return False

# print(linearSearch(lista_aleatoria, e))


#### Búsqueda Binaria
def binarySearch(lista, e):
    if len(lista) == 1:
        return lista[0] == e

    middle = len(lista)//2
    if e == lista[middle]:
        return True
    elif e < lista[middle]:
        return binarySearch(lista[:middle], e)
    else:
        return binarySearch(lista[middle:],e)


# Ordenamiento
#### Ordenamiento Burbuja

def bubble_sort(lista):
    for tope in range(len(lista)-1,0,-1):
        for i in range(tope):
            if lista[i] > lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp

# bubble_sort(lista_aleatoria)

# print(lista_aleatoria)

### MERGE SORT
def merge_sort(lista):
    # print(lista)
    n = len(lista)
    if n > 1:
        izq = lista[:n//2]
        der = lista[n//2:]

        merge_sort(izq)
        merge_sort(der)

        merge(lista, izq, der)

def merge(lista, izq, der):
    i = j = k = 0

    while i<len(izq) and j < len(der):
        if izq[i] > der[j]:
            lista[k] = izq[i]
            i += 1
        else:
            lista[k] = der[j]
            j += 1
        k += 1

    while i < len(izq):
        lista[k] = izq[i]
        i += 1
        k += 1

    while j < len(der):
        lista[k] = der[j]
        j += 1
        k += 1

print(lista_aleatoria)

merge_sort(lista_aleatoria)

print(lista_aleatoria)
