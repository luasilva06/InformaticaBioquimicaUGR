'''Escribir un menú con tres opciones para ejecutar la opción que se desee.
 La forma del menú será la siguiente:
   MENÚ     
 1- calculo de la distancia euclidea entre dos puntos (x1,y1) y (x2,y2)
 2- calculo de distancia D desde un punto (x0,y0) a la linea aX+bY + c = 0
 3 - Área del triangulo definido por  los puntos (x1,y1),(x2,y2) y (x3,y3)
Su opción: 
 '''
 # INICIALIZACION
 
print ("\t\t\t\t Menú \n\t 1 - Calculo de la distancia euclidea\
       \n\t 2 - Calculo de distancia \n\t 3 - Área de el triangulo")
opcion= int(input("Su opción: "))

# OPERACIONES

if (opcion == 1):
    print ("Opción 1 selecionada")
    x1= float(input("Cual es el valor del X1? "))
    x2= float(input("Cual es el valor del X2? "))          
    y1= float(input("Cual es el valor del Y1? "))
    y2= float(input("Cual es el valor del Y2? "))
    distEu = (((x1 - x2) **2) + ((y1 - y2) ** 2)) ** 1/2
    print ("El resultado de la distancia con los valores digitados es {:.2f}"\
           .format(distEu))
        
elif (opcion == 2):
    print ("Opción 2 selecionada")
    x0= float(input("Cual es el valor del punto X0? "))
    y0= float(input("Cual es el valor del punto Y0? "))
    a=int(input("Introduce el valor de a:"))
    b=int(input("Introduce el valor de b:"))
    c=int(input("Introduce el valor de c:"))
    distPun = abs((a * x0)+(b * y0) + c)/(((a ** 2)+(b ** 2)) ** 1/2)
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
else: print("Opcion invalida")