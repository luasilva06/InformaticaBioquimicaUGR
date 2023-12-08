''' Calcular la función “Suma de 0 a n para un número entero positivo 
leído desde teclado, implementando las instrucciones necesarias para el 
cálculo. Por otro lado, calcular la función “Producto de 1 a n” para un número 
entero positivo leído desde teclado.
a- ir al menú de cálculos geometricos
b- ir al menu de calculo de funciones matematicas
c- salir'''

# INICIALIZACION

print ("\t\t\t\t Menú \n\t a - Ir al menú de cálculos geometricos\
       \n\t b - Ir al menú de funciones matematicas \n\t c - Salir")
       
opcion= input("Su opción: ")

# OPERACIONES

##      ANTERIOR
if (opcion == 'a'):
    print ("\t\t\t\t Menú \n\t 1 - Calculo de la distancia euclidea\
           \n\t 2 - Calculo de distancia \n\t 3 - Área de el triangulo\
               \n\t 4 - Salir")
    opcion= int(input("Su opción: "))
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
           
        
        print ("\t\t\t\t Menú \n\t 1 - Calculo de la distancia euclidea\
               \n\t 2 - Calculo de distancia \n\t 3 - Área de el triangulo\
                   \n\t 4 - Salir")
        opcion= int(input("Su opción: "))
     
    print ("Hasta luego") 
 
    
 ##         NUEVO
    
elif (opcion == 'b' ):
    print ("\t\t\t\t Menú \n\t 1 - Soma de 0 a N\ \n\t 2 - producto de 1 a N \
          \n\t 3 - Salir")           
    opcion= int(input("Su opción: "))
    while (opcion != 3):
        if (opcion == 1):
            suma = 0
            numero = int(input("Introduza el valor N de la suma: "))
            for i in range (numero + 1):
                suma = suma + i
            print("El valor de la suma de 0 hasta {} es: {}.\n\n"
                  .format(numero, suma))
            
            print ("\t\t\t\t Menú \n\t 1 - Soma de 0 a N\
                   \n\t 2 - producto de 1 a N \n\t 3 - Salir")           
            opcion= int(input("Su opción: "))
            
        elif (opcion == 2):
            prod = 1
            numero = int(input(" Introduza el valor N del producto: "))
            for i in range (1,numero+1,1):
                prod = prod *i
            print ("El resultado del producto de 1 a {} es: {}.\n\n"
                   .format(numero, prod))
            print ("\t\t\t\t Menú \n\t 1 - Soma de 0 a N\
                   \n\t 2 - producto de 1 a N \n\t 3 - Salir")           
            opcion= int(input("Su opción: "))
    
    print ("Hasta luego")  


else: print("OPCION INVÁLIDA!!")
    
    
    
    
    
    
    