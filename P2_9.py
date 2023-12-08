'''Defina las variables kilo_de_arroz=1,15 y lata_atun=1,50. Calcule:'''
import math as mt
# Inicializacion
kilo_de_arroz=1.15
lata_atun=1.50

# Operaciones
'''a) El precio de tres kilos de arroz y 2 latas de atún'''
a= (3*kilo_de_arroz)+(2*lata_atun)

'''b) Idem a) pero agregue el 18% de IVA'''
b=a*1.18

'''c) Idem b) pero muestre el valor redondeado al euro más próximo'''
c=round(b)

#Salidas
print("Los resultados son: \n \t A :{0:5.2f} \n \t B:{1:5.2f} \n \t C: {2}".format(a,b,c))