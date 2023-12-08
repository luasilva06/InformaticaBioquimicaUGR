'''Pedir uma lista de valores positivos, colocar numa lista. Se colocar negativo termina'''

#INICIALIZACION
lista = []

#OPERACIONES
num = int(input("introduzca el valor positivo que quieres anadir a la lista\
 si poner un valor negativo acaba  "))

while num >= 0:
    lista.append(num)
    num = int(input("introduzca el valor positivo que quieres anadir a la lista\
 si poner un valor negativo acaba  "))

#SALIDAS

print("Usted introduzió un negativo.")
print("La lista es: \n{}".format(lista))

''' Fazer duas listas, uma com pares outra com impares'''
#INICIALIZACION

pares =[]
impares=[]

#OPERACIONES
for i in range(len(lista)):
    if (lista[i] % 2) == 0:
        pares.append(lista[i])
    else:
        impares.append(lista[i])
#SALIDAS        
print("\nPares: \n{}".format(pares))
print("\nImpares: \n{}".format(impares))