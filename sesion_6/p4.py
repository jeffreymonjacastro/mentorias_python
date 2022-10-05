# Strings

frase = input("Ingrese la frase:")
palabra = input("Ingrese la palabra a contar:")

new_frase = ""

for i in frase:
    if i != " " and i != ",":
        new_frase += i

largo = len(palabra)
count = 0

for i in range(len(new_frase)- largo + 1):
    if new_frase[i:i+largo] == palabra:
        count += 1

print(new_frase)
print(f"El numero de veces que aparece la palabra es: {count}")