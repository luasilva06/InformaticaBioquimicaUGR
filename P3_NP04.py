'''Implemente un script que permita, dado un valor entero n, calcular la 
sumatoria 1+2+3+....+n utilizando sentencias repetitivas.'''

# INICIALIZACION

num = int (input ("Cual número entero quieres usar para el ejercicio? " ))
cont = 0
# OPERACIONES & SALIDAS

for i in range (1,num+1):
    cont = cont + i
print ("La sumatoria es: {}".format(cont))
    