'''Un objeto con temperatura inicial 𝑇1 que se coloca en tiempo 𝑡 = 0 en un refrigerador cuya
temperatura constante es 𝑇9, sufrirá un cambio de temperatura dado por la ecuación'''

# INICIALIZACION
import math as mt
k=0.45
temp0 = (120-32)/1.8 #porque tiene que usar °C
tempS = (38-32)/1.8
tiempo1=1*60 #porque es en minutos
tiempo2=2*60
tiempo3=3*60

# OPERACIONES
tempFinal1 = tempS + ((temp0 - tempS)*(mt.e**(-k*tiempo1)))
tempFinal2 = tempS + ((temp0 - tempS)*(mt.e**(-k*tiempo2)))
tempFinal3 = tempS + ((temp0 - tempS)*(mt.e**(-k*tiempo3)))

# SALIDAS
print("La temperatura de una lata despues de 1h es: {}°C".format(round(tempFinal1)))
print("La temperatura de una lata despues de 2h es: {}°C".format(round(tempFinal2)))
print("La temperatura de una lata despues de 3h es: {}°C".format(round(tempFinal3)))
