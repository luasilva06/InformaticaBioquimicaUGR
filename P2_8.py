import math as mt
'''8. Verifique las siguientes identidades trigonométricas asignando previamente los valores
indicados a las variables correspondientes:
Para x = (2/5) P y = 3'''

#Variables
x = (2/5)*mt.pi
y = 3

# Calculos
multiSenXCosY= (mt.sin(x+y)+mt.sin(x-y))/2
multiSenXSenY= (mt.cos(x-y)-mt.cos(x+y))/2

#Salidas
print("sen(x)*cos(y) con los valores de x: {} y: {}. El resultado es: {}".format(x,y,multiSenXCosY))
print("sen(x)*sen(y) con los valores de x: {} y: {}. El resultado es: {}".format(x,y,multiSenXSenY))