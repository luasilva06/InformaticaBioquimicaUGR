import math as mt
'''Convierta las siguientes fórmulas a expresiones en Python (asigne valores a las variables
previamente y haga que los resultados salgan por pantalla al ejecutar el script'''
#Variaveis

x=6
y= 2
cateto1 = 5
cateto2=2
caso1=2
caso2=2
caso3=3
num_casos=3
#formulas

a = (x * y) * (x + y) / 2
'''El item B es llamado de hipo'''
hipo=(((cateto1 ** 2) + (cateto2 ** 2))**0.5)
b=hipo
c= x ** 2 + (x + 1) ** 2 + (x + 2) ** 2
'''item D es llamado de media'''
media= (caso1+caso2+caso3)/num_casos
d=media
'''item E es llamado poli'''
poli= - (x**9) - (2.7*x**6) -(5*x**4) - x + 3.3
e=poli
#Salidas

print("El resultado del item A es: {}\n".format(a))
print("El resultado del item B es: {}\n".format(b))
print("El resultado del item C es: {}\n".format(c))
print("El resultado del item D es: {}\n".format(d))
print("El resultado del item E es: {}\n".format(e))
