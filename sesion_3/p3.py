# Estructuras de control repetitivas

n = int(input("Ingrese el valor de n: "))

suma = 0
i = 1
while i <= n:
    suma += 6/(i**2)
    i += 1

result = suma**0.5
print(f"La suma es: {result}")