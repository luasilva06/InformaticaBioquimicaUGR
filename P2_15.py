import math as mt
'''15. La distancia d desde un punto (x0, y0) a la línea ax+by+c = 0 es [...]
Escriba un script que solicite los valores (x0, y0) y determine la distancia del punto a la línea
3x+5y-2 = 0. Utilice las funciones sqrt y abs. Generalícelo para que funcione con cualquier
línea de la forma ax+by+c = 0.'''

# INICIALIZACION

xo=int(input("Introduce el valor de x0:"))
yo=int(input("Introduce el valor de y0:"))
a=int(input("Introduce el valor de a:"))
b=int(input("Introduce el valor de b:"))
c=int(input("Introduce el valor de c:"))

# OPERACIONES

dis=abs((a*xo)+(b*yo)+c)/mt.sqrt((a**2)+(b**2))

# SALIDA

print("La distancia es: {}".format(dis))
