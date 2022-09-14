# Uso de expresiones

a = int(input("Ingrese el lado a: "))
b = int(input("Ingrese el lado b: "))
c = int(input("Ingrese el lado c: "))

cosx = (b**2 + c**2 - a**2)/(2*b*c)
cosy = (a**2 + c**2 - b**2)/(2*a*c)
cosz = (a**2 + b**2 - c**2)/(2*a*b)

comprobacion = (cosx > 0) and (cosy > 0) and (cosz > 0)

resultado = "El triángulo es acutángulo"*(comprobacion == True) + "El triángulo no es acutángulo"*(comprobacion == False)

print(resultado)
