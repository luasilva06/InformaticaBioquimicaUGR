import math as mt
'''El número de combinaciones posibles Cn,r para tomar r objetos de un conjunto de n se define
como Cn,r = n! / (r! * ((n-r)!). Escriba un script que solicite los valores de n y r
 y calcule Cn,r (utilice la funcion “factorial”)'''

# INICIALIZACION

n =int(input("Cual es el valor de n? Digite ->"))
r=int(input("Cual es el valor de r? Digite ->"))


# OPERACIONES

comb= mt.factorial(n)/(mt.factorial(r)*mt.factorial(n-r))

# SALIDAS

print("El número de combinaciones posibles con N igual a  {} e R igual a {} es: {}".format(n,r,comb))