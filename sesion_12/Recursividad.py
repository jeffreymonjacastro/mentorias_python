# Función suma
a = 5

# Forma iterativa
sum = 0
for i in range(1,a+1):
    sum += i

print(sum)

# Forma recursiva
def suma(n):
    if n == 1:
        return 1
    else:
        return n + suma(n-1)

print(suma(a))

# Fórmula
print((a*(a+1))/2)

# Factorial
n = int(input("N: "))

# Forma iterativa
fact = 1
for i in range(1, n+1):
    fact *= i

print(fact)

# Forma recursiva
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(n))

