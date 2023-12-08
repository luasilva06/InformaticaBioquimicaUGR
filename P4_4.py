'''4.- Una vez que la matriz de distancias ha sido creada correctamente,
dicho programa debe realizar las siguientes operaciones a seleccionar mediante 
un menú:
   '1. Cambiar de proteína'
   '2. Átomos a menos de d Angstroms de uno dado'
   '3. Distancias por debajo de un umbral'
   '4. Terminar'.'''
import Bio.PDB as pdb
import numpy as np
   
fichero = input("Nombre del fichero de la protei­na (sin extension): ")
fichero += '.pdb'
parser = pdb.PDBParser()
try:
    s = parser.get_structure('my_pdb', fichero)
except:
    s = parser.get_structure('my_pdb', '1clg.pdb') #fichero por defecto

# OPERACIONES PARA OBTENER LAS COORDENADAS

ats_global = []
ats_info = []
ats_chains = []
for model in s:
    for chain in model:
        cadena = []
        for residue in chain:
            for atom in residue:
               ats_global.append(list(atom.get_coord()))
               cadena.append(list(atom.get_coord()))
               ats_info.append([atom.get_name(),atom.get_id()])
        ats_chains.append(cadena)

#num_ats = len(ats_global)
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
       
distanciasAbajo = distancias.T  
distFinal = distancias + distanciasAbajo     

 

print("\t MENU \n 1 - Cambiar de proteía \n 2 - Átomos a menos de d Angstroms de un dado\
\n 3 - Distancias por debajo de un umbral \n 4 - TERMINAR")    
opc = int(input("Cual es la opcion? "))

while opc!= 4:
    
    if opc == 1: 
        
        
        fichero = input("Nombre del fichero de la protei­na (sin extension): ")
        fichero += '.pdb'
        parser = pdb.PDBParser()
        try:
            s = parser.get_structure('my_pdb', fichero)
        except:
            s = parser.get_structure('my_pdb', '1clg.pdb') #fichero por defecto

        # OPERACIONES PARA OBTENER LAS COORDENADAS

        ats_global = []
        ats_info = []
        ats_chains = []
        for model in s:
           for chain in model:
               cadena = []
               for residue in chain:
                   for atom in residue:
                      ats_global.append(list(atom.get_coord()))
                      cadena.append(list(atom.get_coord()))
                      ats_info.append([atom.get_name(),atom.get_id()])
               ats_chains.append(cadena)

       
        distancias = np.zeros ((len(ats_global),len(ats_global)))  #criando uma tabla para aguardar os valores
        # OPERACIONES

       
        for i in range(len(ats_global)): #
            
            for j in range(i+1,len(ats_global)): 
                distX = ((ats_global[i][0]) - (ats_global[j][0]))**2
                distY = ((ats_global[i][1]) - (ats_global[j][1]))**2
                distZ = (ats_global[i][2] - ats_global[j][2])**2
                
                
                distEu = ((distX + distY + distZ) ** (1/2))
                distancias [i,j] = distEu
               
        distanciasAbajo = distancias.T  
        distFinal = distancias + distanciasAbajo
        
        print("\t MENU \n 1 - Cambiar de proteía \n 2 - Átomos a menos de d Angstroms de un dado\
        \n 3 - Distancias por debajo de un umbral \n 4 - TERMINAR")    
        opc = int(input("Cual es la opcion? "))
     
    elif (opc == 2):
        
          
            ##  2. Átomos a menos de d Angstroms de uno dado'     
        # =============================================================================
        print(distFinal)
        maximo = distFinal.max()
        minimo = maximo
        for a in distFinal: # calcular o minimo percorrendo tudo
             for b in a:
                if (b < minimo) and (b != 0):
                     minimo = b                
         
        print ("la distancia minima es {} y la maxima es {}".format(minimo, maximo))
         
        cercanos = [] # guardar el indice del punto menor
        protag = int(input("Cual es el punto de la matriz que queires comparar?"))
        umbralDist =  float(input("Cual es el umbral?"))
        infors = []
         
        for k in range(len(distancias)):
            
            if (distFinal[protag][k] < umbralDist) and  (protag != k):
                
                cercanos.append(k)
         
        for c in cercanos:
            
            
            print(ats_info[c])
         
        print("\t MENU \n 1 - Cambiar de proteía \n 2 - Átomos a menos de d Angstroms de un dado\
        \n 3 - Distancias por debajo de un umbral \n 4 - TERMINAR")    
        opc = int(input("Cual es la opcion? "))      
    # =============================================================================

    
    elif (opc == 3):
        
        
    ## 3. Distancias por debajo de un umbral'
        maximo = distFinal.max()
        minimo = maximo
        for a in distFinal: # calcular o minimo percorrendo tudo
            for b in a:
                if (b < minimo) and (b != 0):
                    minimo = b
                
        
        print ("la distancia minima es {} y la maxima es {}".format(minimo, maximo))
        listita= [] # guardar el indice del punto menor
        
        umbralDist =  float(input("Cual es el umbral? "))
        print("3' \t     5' \n ")
        for w in range(len(distFinal)):
            for k in range(w+1,len(distFinal)) :
                if (distFinal[w][k] < umbralDist):        
                    listita.append([w, k])
                    print("{} \t  \t {}".format(w,k))
        
       
        
        print("\t MENU \n 1 - Cambiar de proteía \n 2 - Átomos a menos de d Angstroms de un dado\
        \n 3 - Distancias por debajo de un umbral \n 4 - TERMINAR")    
        opc = int(input("Cual es la opcion? "))


print("HASTA LUEGO!!")







