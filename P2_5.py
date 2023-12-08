import math as mt
''' 5. La fórmula para cambiar la base de un logaritmo es
logaN=logbN/logbA'''
# a) utilice la función log(x) para calcular log5 73 x log2 55,23
calculoA= mt.log(73,5)*mt.log(55.23,2)
print("El resultado del item A es: {}".format(calculoA))
# b) utilice la función log10(x) para calcular log7 21 – log4 423
calculoB= mt.log(21,7)- mt.log(423,4)
print("El resultado del item B es: {}".format(calculoB))