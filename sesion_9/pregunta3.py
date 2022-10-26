def funcionA(lista):
    new_lista = [i for i in lista if i[-1] in "aeiou"]
    print(new_lista)

def funcionB(lista):
    new_lista = [i for i in lista if len(i) == 5]
    print(new_lista)

def funcionC(matriz):
    

    new_lista = [matriz[i][j] for i in range(len(matriz)) for j in range(len(matriz[0])) if matriz[i][j] > 10]


    print(len(new_lista))


lista1 = ["lapiz" ,"borrador" ,"regla" ,"lapicero"]

matriz = [[15 ,2 ,3] ,[4 ,12 ,6] ,[7 ,8 ,19]]

funcionA(lista1)
funcionB(lista1)

funcionC(matriz)
