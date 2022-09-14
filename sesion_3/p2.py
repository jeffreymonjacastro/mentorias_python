# Estructuras de control selectivas

# Entrada
anio1 = int(input("Ingrese el primer anio: "))
anio2 = int(input("Ingrese el primer anio: "))

# Operaciones
# Primer año:
a = anio1%19
b = anio1%4
c = anio1%7
d = (19*a + 24)%30
e = (2*b + 4*c + 6*d + 5)%7
n = (22 + d + e)

# Segundo año:
A = anio2%19
B = anio2%4
C = anio2%7
D = (19*A + 24)%30
E = (2*B + 4*C + 6*D + 5)%7
N = (22 + D + E)

# IF
if n == N:
    print("Ambos anios tienen la misma fecha de Pascua")

    if n <= 31:
        print(f"El domingo de Pascua es el {n} de marzo")
    else:
        print(f"El domingo de Pascua es el {n - 31} de abril")

else:
    print("Los anios tienen distinta fecha de Pascua")

    if n <= 31:
        print(f"El domingo de Pascua del primer anio es el {n} de marzo")
    else:
        print(f"El domingo de Pascua del primer anio es el {n-31} de abril")

    if N <= 31:
        print(f"El domingo de Pascua del segundo anio es el {N} de marzo")
    else:
        print(f"El domingo de Pascua del segundo anio es el {N-31} de abril")
