'''Hacer un script que pida al usuario el límite inferior y superior de un
 intervalo de números enteros [inf, sup] y que imprima por pantalla todos los 
 números pares comprendidos entre ellos utilizando sentencias repetitivas.'''

#INICIALIZACION

limInf = int(input(" Digite el limite inferior: "))
limSup= int(input(" Digite el limite superior: "))
par= 0

#Operaciones & Salidas

for i in range (limInf,limSup+1,1):
    if i%2 == 0:
        print ("{} es par ". format(i))
        
