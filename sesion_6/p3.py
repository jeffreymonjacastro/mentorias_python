## Coprimos

def coprimos(n):
    string = ""

    for i in range(2, n + 1):
        count = 0

        for j in range(1, n):
            if i % j == 0 and n % j == 0:
                count += 1

        if count == 1:
            string += str(i) + " "

    return string


while True:
    n = int(input("Ingrese su numero:"))

    if n > 0:
        break

print(f"Los numeros coprimos y menores a {n} son:")
print(coprimos(n))