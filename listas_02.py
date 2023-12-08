'''Fazer um codigo que calcule a distancia euclidia entre los puntos'''
import numpy as np
# INICIALIZACION
puntos = [2,3,0],[1,1,1],[0,0,0],[4,3,1]
distancias = np.zeros ((len(puntos),len(puntos)))  #criando uma tabla para aguardar os valores
# OPERACIONES

# D = (((x1-x2)**2) + ((y1-y2)**2) + ((Z1 - Z2)**2)) ** 1/2
for i in range(len(puntos)): # correu os valores macro
    
    for j in range(i+1,len(puntos)): # correr os micro e a uma posição a mais, para não repetir
        distX = (puntos[i][0] - puntos[j][0])**2
        distY = (puntos[i][1] - puntos[j][1])**2
        distZ = (puntos[i][2] - puntos[j][2])**2
        
        
        distEu = ((distX + distY + distZ) ** (1/2))
        distancias [i,j] = distEu
        #print("La distancia entre los puntos {} y {} es {:.2f}".format(puntos[i][i],puntos[j][i],distEu))
distanciasAbajo = distancias.T  
distFinal = distancias + distanciasAbajo     
#SALIDAS
       #print("La distancia entre los puntos es: {:.2f}".format(distEu))
     
print(distFinal)


''' Colocar em uma nova variavel os pontos mais proximos de um punto x da matriz'''
cercanos= [] # guardar el indice del punto menor
protag = int(input("Cual es el punto de la matriz que queires comparar?"))
umbralDist =  float(input("Cual es el punto de la matrix que queires comparar?"))

for k in range(len(distancias)):
    if (distFinal[protag][k] < umbralDist) and  (protag != k):
        
        cercanos.append(k)

print(cercanos)