'''7. Asigne valores a tres variables. Escriba los comandos necesarios para intercambiar los valores
de las tres variables de manera que el valor de la primera acabe en la segunda, el de la
segunda en la tercera y el de la tercera en la primera. Muestre el contenido final de las tres
variables.'''

# Asignando

n1= 1
n2= 2
n3= 3

#Calculos

z = n1+n2+n3
n1= z -(n1+n2) # ahora tiene el valor de n3
n2 = z - (n2+n3) # ahora tiene el valor de n1
n3 = z - (n1+n2) # ahora tiene el valor de n2

# Salida

print("Antes el N1 era 1, ahora es {}".format(n1))
print("Antes el N2 era 2, ahora es {}".format(n2))
print("Antes el N3 era 3, ahora es {}".format(n3))