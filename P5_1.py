'''1. Implementar una función llamada matriz_distancias que reciba la matriz 
completa de átomos ats_global y devuelva la correspondiente matriz de
distancias, de manera que pueda llamarse de la siguiente manera:
                d = matriz_distancias(ats_global)'''
                
def matriz_distancias(ats_global):
    """
    Parameters
    ----------
        glob necesita ser una lista con coordenadas para que se pueda calcular las distancias
    Returns
    -------
        Distancia entre atomos de una proteina en una matriz
        
    Requires
    --------
        Ya debe tener ats_global (parametro) ya listo
        importar Numpy
    """
   
    import numpy as np   
    
    distancias = np.zeros ((len(ats_global),len(ats_global)))  #criando uma tabla para aguardar os valores
    # OPERACIONES

    # D = (((x1-x2)**2) + ((y1-y2)**2) + ((Z1 - Z2)**2)) ** 1/2
    for i in range(len(ats_global)): # correu os valores macro
        
        for j in range(i+1,len(ats_global)): # correr os micro e a uma posiÃ§Ã£o a mais, para nÃ£o repetir
            distX = ((ats_global[i][0]) - (ats_global[j][0]))**2
            distY = ((ats_global[i][1]) - (ats_global[j][1]))**2
            distZ = (ats_global[i][2] - ats_global[j][2])**2
            
            
            distEu = ((distX + distY + distZ) ** (1/2))
            distancias [i,j] = distEu
            #print("La distancia entre los puntos {} y {} es {:.2f}".format(puntos[i][i],puntos[j][i],distEu))
    distanciasAbajo = distancias.T  
    distFinal = distancias + distanciasAbajo     
    
    return distFinal
                 
           