l = []
while True:
    n = int(input("Numero: "))

    if n == 0:
        break
    else:
        l.append(n)

mitad = len(l)//2

sublista1 = l[:mitad]
sublista2 = l[mitad:]

if len(l) % 2 == 0:
    for i in range(mitad):
        print(sublista1[mitad-1-i], end=" ")
        print(sublista2[i], end=" ")
else:
    print(sublista2[0], end=" ")

    for i in range(mitad):
        print(sublista1[mitad-1-i], end=" ")
        print(sublista2[i+1], end=" ")
