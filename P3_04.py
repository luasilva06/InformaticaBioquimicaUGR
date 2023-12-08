'''Incluya una quinta opción en el menú anterior con el siguiente 
texto '4. Salir'. El programa debe permitir al usuario estar realizando cálculos 
repetitivamente mientras quiera, y sólo terminará cuando el usuario
indique la opción de salida.'''

# INICIALIZACION

print ("\t\t\t\t Menú \n\t 1 - Calculo de la distancia euclidea\
       \n\t 2 - Calculo de distancia \n\t 3 - Área de el triangulo\
           \n\t 4 - Salir")
opcion= int(input("Su opción: "))

# OPERACIONES
while (opcion !=4):

    if (opcion == 1):
        print ("Opción 1 selecionada")
        x1= float(input("Cual es el valor del X1? "))
        x2= float(input("Cual es el valor del X2? "))          
        y1= float(input("Cual es el valor del Y1? "))
        y2= float(input("Cual es el valor del Y2? "))
        distEu = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 1/2
        print ("El resultado de la distancia con los valores digitados es {:.2f}"\
               .format(distEu))
            
            
    elif (opcion == 2):
        print ("Opción 2 selecionada")
        x0= float(input("Cual es el valor del punto X0? "))
        y0= float(input("Cual es el valor del punto Y0? "))
        a=int(input("Introduce el valor de a:"))
        b=int(input("Introduce el valor de b:"))
        c=int(input("Introduce el valor de c:"))
        distPun = abs((a * x0) + (b * y0) + c) / (((a ** 2) + (b ** 2)) ** 1/2)
        print ("El resultado de la distancia con los valores digitados es {:.2f}"\
              .format(distPun))
        
    elif (opcion == 3):
        print ("Opcion 3 selecionada")
        x1= float(input("Cual es el valor del X1? "))
        y1= float(input("Cual es el valor del Y1? "))
        x2= float(input("Cual es el valor del X2? "))
        y2= float(input("Cual es el valor del Y2? "))
        x3= float(input("Cual es el valor del X3? "))
        y3= float(input("Cual es el valor del Y3? "))
        areaTr = 1 / 2 * (abs(x1 * (y2 - y3)) + x2 * (y3 - y1) + x3 * (y1 - y2))
        print ("El resultado de la area con los valores digitados es {:.2f}"\
              .format(areaTr))
       
   # elif (opcion == 4):
    #    print("Hasta luego!")
    
    print ("\t\t\t\t Menú \n\t 1 - Calculo de la distancia euclidea\
           \n\t 2 - Calculo de distancia \n\t 3 - Área de el triangulo\
               \n\t 4 - Salir")
    opcion= int(input("Su opción: "))
 
print("Hasta luego!")    