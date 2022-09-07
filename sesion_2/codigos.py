true = (("a" == "b") or (3.14 < 3*2)) * "Hello World"

print(type(true))

### EJERCICIOS

## IF ELSE
# Ejercicio 1

"""
Números enteros
Escribir un programa que permita leer como dato un
número entero y luego imprima si es positivo,
negativo o es cero
"""

num = int(input("Ingrese un numero entero: "))

if num > 0:
    print(f"El número {num} es positivo")
elif num < 0:
    print(f"El número {num} es negativo")
else:
    print(f"El número {num} es cero")

# fprint o comas
nombre = "Jeffrey"
apellido = "Monja"
edad = "17"
carrera = "CS"

print(f"Hola, me llamo {nombre} {apellido}. Tengo {edad} años y estudio la carrera de {carrera}")


# Ejercicio 2

"""
Días de la semana
Escribir un programa en Python que permita ingresar
un número del 1 - 7 y muestre su equivalente en letras
Ejemplo 1 = 2 Martes, etc si esta fuera de rango, mostrar el mensaje "error"
"""

num_semana = int(input("Número de la semana: "))

if num_semana == 1:
    print("Lunes")
elif num_semana == 2:
    print("Martes")
elif num_semana == 3:
    print("Miércoles")
elif num_semana == 4:
    print("Jueves")
elif num_semana == 5:
    print("Viernes")
elif num_semana == 6:
    print("Sábado")
elif num_semana == 7:
    print("Domingo")
else:
    print("Error")


# Ejercicio 3

"""
Edad mayor
Escribir un programa en Python que permita ingresar 
3 edades e indique cuál es el mayor
"""

edad_a = int(input("Edad a: "))
edad_b = int(input("Edad b: "))
edad_c = int(input("Edad c: "))

if edad_a > edad_b:
    if edad_a > edad_c:
        print("La mayor edad es:", edad_a)
    else:
        print("La mayor edad es:", edad_c)
else:
    if edad_b > edad_c:
        print("La mayor edad es:", edad_b)
    else:
        print("La mayor edad es:", edad_c)


## si queremos hallar de mayor a menor
result = ""

if edad_a > edad_b:
    if edad_a > edad_c:
        result = result + str(edad_a) + ", "

        if edad_b > edad_c:
            result = result + str(edad_b) + ", "
        else:
            result = result + str(edad_c) + ", "
    else:
        result = result + str(edad_c) + ", "

    result = result + str(edad_a) + ", " + str(edad_b)
else:
    if edad_b > edad_c:
        result = result + str(edad_b) + ", "

        if edad_a > edad_c:
            result = result + str(edad_a) + ", "
        else:
            result = result + str(edad_c) + ", "
    else:
        result = result + str(edad_c) + ", "

    result = result + str(edad_b) + ", " + str(edad_a)

print(result)


## WHILE

# Ejercicio 1
"""
Números impares
Diseñe e implemente un algoritmo en Python que permita al usuario ingresar un número, 
y el algoritmo debe imprimir los números impares, desde uno hasta el número ingresado.
"""

num = int(input("Ingrese un número: "))

contador = 1
while contador <= num:
    print(contador)

    contador += 2


# Ejercicio 2
"""
Factorial n
Escribir un programa que permita leer como dato un número entero 
y luego imprima el factorial de este número. Ojo: n! = 1x2x3x...x(n-1)xn
"""

n = int(input("Ingrese el número: "))

i = 1
factorial = 1

while i <= n:
    factorial *= i  # factorial = factorial + i

    i += 1  # i = i + 1

print(factorial)


# Ejercicio 3

"""
Validación de entrada
Desarrolle un programa que permita validar el ingreso de un número entero que 
esté dentro del rango 1 - 10. Si el número está fuera del rango, se deberá
volver a pedir ingresar el número. Y al terminar, imprimir una carita ":D"
"""

n = int(input("Ingrese el número: "))
count = 0

while n < 1 or n > 10:
    n = int(input("Ingrese el número: "))
    count += 1

print(count)


while True:
    n = int(input("Ingrese el número: "))

    if n <= 10 and n >= 1:
        break


print(":D")
