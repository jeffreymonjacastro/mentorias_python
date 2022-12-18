# d = {1: {10:"A", 20:"B"}, 2: {"Mundo":"World"}, 3:{'A':"Soy", 'B':"Yo", 'C':"Denuevo"}}
#
# print(d[1], d[2], d[3]['A'], d[3]['B'], d[3]['C'])
#
# for key, value in d.items():
#     print("Llave:", key)
#
#     for subkeys in value:
#         print("Subllave: ", subkeys, " valor: ", value[subkeys])
#
#

import json

import pandas as pd

d_estudiante = {
    'estudiante001':{
        'nombre': "Juamchimy",
        'codigo': 202210777,
        'carrera': "CS"
    },

    'estudiante002':{
        'nombre': "Jeff",
        'codigo': 202210999,
        'carrera': "Meca",
        'notas': [19, 19, 20]
    }
}

# with open("data.json", 'w') as archivojs:
#     json.dump(d_estudiante, archivojs)
#
# with open("data.json") as datafile:
#     data = json.load(datafile)
#
# print(data)

import pandas

# data = pd.read_csv("data.csv")
# print(data[['nombre', 'carrera']])

datos = open("disco.txt", "r")

for fila in datos:
    print(datos)