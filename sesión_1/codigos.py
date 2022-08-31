# Sesión 1

# Librerías
import math

# input("Ingresen datos: ")

# print("Hola Mundo")

a = 5
b = 3.14
c = "Hola"
d = True # Es igual a 1
e = False # Es igual a 0

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b) # División exacta
# print(a//b) # División entera (cociente)
# print(a%b) # Residuo de la división
# print(a**b) # Potencia

# Operaciones Combinadas
# print(5**2+3)
# print(5-4//2)
# print((4+3)*2)

# Librería Math
# print(4**0.5)
# print(math.sqrt(4))
# print(math.pow(2,4))
# print(math.pi)

# Operadores lógicos
# Not -> Cambia el valor de verdad de la afirmación
# a = False
# b = True
#
# print(a and b and b and b and b and b)

# Operadores de relación

# a = (7.4 != 7.4) and (4 <= 3)
#
# print(a)


# Problema 1:

# num = int(input("Número: "))
#
# unidad = num % 10
# decena = (num // 10) % 10
# centena = num // 100
#
# result = unidad*100 + decena*10 + centena
#
# print(result)
# print("Python" * 100)

# Problema 2

# num = int(input("Number: "))
#
# result = (num % 2 == 0)*"Es par" + (num % 2 == 1)*"Es impar"
#
# print(result)

# Problema 3
#
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))
#
# resultado = (((a+b > c) and (b+c > a) and (a+c > b)) == True)*"ES TRIÁNGULO VÁLIDO" + (((a+b > c) and (b+c > a) and (a+c > b)) == False)*"NO ES TRIÁNGULO VÁLIDO"
#
# print(resultado)

# Problema bonus
## input: Numero en segundos
## Output: numero formato dd::hh:mm:ss

num = int(input("Segundos: "))

dias = num // 86400

num = num % 86400

horas = num // 3600

num = num % 3600

minutos = num // 60
seg = num % 60

print(f"{dias}:{horas}:{minutos}:{seg}")
print(dias, ":", horas, ":",minutos,":",seg)
