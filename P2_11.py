'''. Escriba un script que pida un valor entero, y muestre su división por 5 y su valor elevado a 3.
Utilice print para mostrar el resultado en el formato adecuado junto con su descripción.'''

# INICIALIZACION

n1= int(input("Introduce un numero entero"))

# OPERACIONES

div1= n1/5
ele1= n1**3

# SALIDAS

print("El numero fue: {}.\nSu division por 5 es {}.\nCuando elevado a 3 es {}".format(n1,div1,ele1))