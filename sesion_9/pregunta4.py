frase = input("Ingrese una frase:")

palabras = frase.split()

d_palabras = {}
d_caracteres = {}

for i in palabras:
    if i not in d_palabras.keys():
        d_palabras[i] = 1
    else:
        d_palabras[i] += 1

for i in frase:
    if i not in d_caracteres.keys():
        d_caracteres[i] = 1
    else:
        d_caracteres[i] += 1

# output
print(f"El numero total de palabras es: {sum(d_palabras.values())}")
print(f"El numero de palabra distintas es: {len(d_palabras.keys())}")
print(f"El numero total de caracteres utilizados es: {sum(d_caracteres.values())}")
print(f"El numero total de caracteres diferentes utilizados es: {len(d_caracteres.keys())}")

