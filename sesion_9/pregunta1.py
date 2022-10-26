frase = input("Ingrese una frase:")

palabras = frase.split()

lista_ar = []
lista_er = []
lista_ir = []

for i in palabras:
    if len(i) >= 2:
        subtring = i[-2] + i[-1]

        if subtring == "ar":
            lista_ar.append(i)
        elif subtring == "er":
            lista_er.append(i)
        elif subtring == "ir":
            lista_ir.append(i)


if len(lista_er) != 0:
    print(f"Los verbos que presentan la conjugacion er son: {lista_er}")
else:
    print("No hay verbos con conjugacion er")

if len(lista_ir) != 0:
    print(f"Los verbos que presentan la conjugacion er son: {lista_ir}")
else:
    print("No hay verbos con conjugacion ir")

if len(lista_ar) != 0:
    print(f"Los verbos que presentan la conjugacion er son: {lista_ar}")
else:
    print("No hay verbos con conjugacion ar")


