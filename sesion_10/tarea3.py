import imageio
import numpy as np


def leer_imagen(ruta):
    """
    La función leer_imagen recibe un string con la ruta
    de una imagen en formato BMP y retorna una lista de
    tres dimensiones con el mapa de bits de la imagen.
    Asimismo, convertimos la lista de numpy a una lista
    común y corriente.
    """
    np_array = np.array(imageio.imread(ruta), dtype='int')
    # noinspection PyTypeChecker
    lista_3d = np_array.tolist()
    return lista_3d


def guardar_imagen(ruta, lista_3d):
    """
    La función guardar_imagen recibe una lista de 3
    dimensiones con el mapa de bits de la imagen
    y retorna la imagen en formato bmp.
    """
    return imageio.imwrite(ruta, np.array(lista_3d, dtype='uint8'))


def oscurecer(lista_3d, pct):
    global new_rojo
    result = list()
    # SU SOLUCIÓN EMPIEZA AQUÍ

    filas = len(lista_3d)
    columnas = len(lista_3d[0])

    for i in range(filas):
        fila = []

        for j in range(columnas):
            red = lista_3d[i][j][0]
            green = lista_3d[i][j][1]
            blue = lista_3d[i][j][2]

            fila.append([blue, green, red])

        result.append(fila)

    # SU SOLUCIÓN TERMINA AQUÍ
    return result


### PARA GENERAR Y PROBAR SUS IMAGENES
lista_3d = leer_imagen("playita.bmp")

Matriz_oscurecer = oscurecer(lista_3d, 60)

guardar_imagen("playitaMovida.bmp", Matriz_oscurecer)







def difuminado(lista_3d):
    result = [row.copy() for row in lista_3d]
    # SU SOLUCIÓN EMPIEZA AQUÍ

    # SU SOLUCIÓN TERMINA AQUÍ
    return result


def cuadrantes(lista_3d, orden):
    result = list()
    # SU SOLUCIÓN EMPIEZA AQUÍ

    # SU SOLUCIÓN TERMINA AQUÍ
    return result

# [1, 2, 3, 4]
matriz1 = np.array([[1,2,3],[4,5,6]])
matriz2 = np.array([[7,8,9],[10,11,12]])

matriz3 = np.array([[13,14,15],[16,17,18]])
matriz4 = np.array([[19,20,21],[22,23,24]])

# [4, 3, 2, 1]
new_matriz1 = np.concatenate((matriz4, matriz3), axis=1)
new_matriz2 = np.concatenate((matriz2, matriz1), axis=1)

final_matriz = np.concatenate((new_matriz1, new_matriz2))

print(final_matriz)
