"""Programa para determinar de tres numeros enteros: sí la suma de los dos primeros es igual al tercero"""

print("--------------------------------")
print("----------x + y = z ------------")
print("--------------------------------")

#Input
x = int(input("Ingrese el valor del primer numero entero: "))
y = int(input("Ingrese el valor del segundo numero entero: "))
z = int(input("Ingrese el valor del tercer numero entero: "))

#Processing
if x + y == z:
    msj = "La suma del primer numero: " + str(x) + " con el segundo numero: " + str(y) + " es el tercer numero: " + str(z)
else:
    msj = "La suma del primer numero: " + str(x) + " con el segundo numero: " + str(y) + " NO ES EL TERCER NUMERO: " + str(z)

#Output
print(msj)