'''
P1  e P2 numero de individuos das populações
alfa e beta é a relação entre as especies
numero de voltas (FOR) é a subtração do ano final e inicial
guardar o p1 numa otra variavel antes da operação, para poder adicionar 
corretamente no p2.          aux = p1'''

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
    print ("\t\t\t\t Menú \n\t 1 - Soma de 0 a N\n\t 2 - producto de 1 a N \
          \n\t 3 - Evolución de poblaciones en un periodo de tiempo\
              \n\t 4 - Salir")           
    opcion= int(input("Su opción: "))
    while (opcion != 4):
        if (opcion == 1):
            suma = 0
            numero = int(input("Introduza el valor N de la suma: "))
            for i in range (numero + 1):
                suma = suma + i
            print("El valor de la suma de 0 hasta {} es: {}.\n\n"
                  .format(numero, suma))
            
            print ("\n\n\t\t\t\t Menú \n\t 1 - Soma de 0 a N\
                   \n\t 2 - producto de 1 a N  \n\t 3 - Evolución de \
                       poblaciones en un periodo de tiempo\
                      \n\t 4 - Salir")           
            opcion= int(input("Su opción: "))
            
        elif (opcion == 2):
            prod = 1
            numero = int(input(" Introduza el valor N del producto: "))
            for i in range (1,numero+1,1):
                prod = prod *i
            print ("El resultado del producto de 1 a {} es: {}.\n\n"
                   .format(numero, prod))
            print ("\n\n\t\t\t\t Menú \n\t 1 - Soma de 0 a N\
                   \n\t 2 - producto de 1 a N  \n\t 3 - Evolución de \
                       poblaciones en un periodo de tiempo\
                      \n\t 4 - Salir")           
            opcion= int(input("Su opción: "))
            
            
        elif (opcion == 3):
            p1 = float(input("Introduza es el tamaño inicial de la\
                             populacion 01: "))
            p2 = float(input("Introduza es el tamaño inicial de la \
                             populacion 02: "))
            r1 = float(input("Introduza es el factor de crescimento de la \
                             populacion 01: "))
            r2 = float(input("Introduza es el factor de crescimento de la \
                             populacion 02: "))
            k1 = int(input("Introduza es la capacidad del medio de la \
                             populacion 01: "))
            k2 = int(input("Introduza es la capacidad del medio de la \
                             populacion 02: "))
            alfa = float(input("Introduza es el efecto de la populacion 2 en la \
                             populacion 01: "))
            beta = float(input("Introduza es el efecto de la populacion 1 en la \
                             populacion 02: "))
            anoInicial = int(input("Introduza es el año inicial: "))
            anoFinal = int(input("Introduza es el año final: "))                 
            aux = p1
            p1I= p1
            p2I = p2
            
            for i in range (anoInicial+1,anoFinal+1,1):
                p1 = p1 + r1 * p1
                aux = p1
                p1 = p1 + r1 * p1 * (k1 - p1 - alfa *p2) / k1              
                p2 = p2 + r2 * p2 * (k2 - p2 - beta * aux) / k2
            print("La populacion 01 es: {} \n\t La populacion 02 es {}"
                  .format(round(p1),round(p2))
                
                
            print ("\n\n\t\t\t\t Menú \n\t 1 - Soma de 0 a N\
                   \n\t 2 - producto de 1 a N  \n\t 3 - Evolución de \
                       poblaciones en un periodo de tiempo \n\t 4 - Salir")           
            opcion= int(input("Su opción: "))         
                                                  
            
            
    
    print ("Hasta luego")  

else: print("OPCION INVÁLIDA!!")
    