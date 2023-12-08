'''Implemente un script que le permita al usuario mostrar la tabla de
 multiplicar de un número que elija. Cuando el número elegido sea cero,
 el script finalizará. Ampliar para que muestre las tablasde multiplicar 
 desde el 1 hasta el 10 con una pausa entre cada tabla.'''
 
             #Inicializacion 
num = int(input("Cual es el número que deseja usar para la tabla? "))

             # OPERACIONES & SALIDAS
while num!= 0:
    for i in range (1,11):
        print ("{} X {} --- {}".format(num,i,num * i))
    num = int(input("\nCual es el número que deseja usar para la tabla? "))
print("Usted digitó 0")