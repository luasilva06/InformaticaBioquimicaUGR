'''5.1 Pintar los ﾃ｡tomos para cada cadena en distintos colores'''

import matplotlib.pyplot as plt
import numpy as np
import Bio.PDB as pdb

fichero = input("Nombre del fichero de la proteiﾂｭna (sin extension): ")
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
               ats_info.append([atom.get_name(),atom.get_id()])
               cadena.append(list(atom.get_coord()))
        ats_chains.append(cadena)

#num_ats = len(ats_global)
distancias = np.zeros ((len(ats_global),len(ats_global)))  #criando uma tabla para aguardar os valores
# OPERACIONES

# D = (((x1-x2)**2) + ((y1-y2)**2) + ((Z1 - Z2)**2)) ** 1/2
for i in range(len(ats_global)): # correu os valores macro
    
    for j in range(i+1,len(ats_global)): # correr os micro e a uma posi鈬o a mais, para nﾃδ｣o repetir
        distX = ((ats_global[i][0]) - (ats_global[j][0]))**2
        distY = ((ats_global[i][1]) - (ats_global[j][1]))**2
        distZ = (ats_global[i][2] - ats_global[j][2])**2
        
        
        distEu = ((distX + distY + distZ) ** (1/2))
        distancias [i,j] = distEu
       
distanciasAbajo = distancias.T  
distFinal = distancias + distanciasAbajo     

 

print("\t MENU \n 1 - Cambiar de proteﾃｭa \n 2 - ﾃ》omos a menos de d Angstroms de un dado\
\n 3 - Distancias por debajo de un umbral \n 4 - TERMINAR")    
opc = int(input("Cual es la opcion? "))

while opc!= 5:
    
# =============================================================================
#     if opc == 1: 
#         
#         
#         fichero = input("Nombre del fichero de la proteiﾂｭna (sin extension): ")
#         fichero += '.pdb'
#         parser = pdb.PDBParser()
#         try:
#             s = parser.get_structure('my_pdb', fichero)
#         except:
#             s = parser.get_structure('my_pdb', '1clg.pdb') #fichero por defecto
# 
#         # OPERACIONES PARA OBTENER LAS COORDENADAS
# 
#         ats_global = []
#         ats_info = []
#         ats_chains = []
#         for model in s:
#             for chain in model:
#                 for residue in chain:
#                     for atom in residue:
#                        ats_global.append(list(atom.get_coord()))
#                        ats_info.append([atom.get_name(),atom.get_id()])
#                 ats_chains.append([ats_global])
# 
#        
#         distancias = np.zeros ((len(ats_global),len(ats_global)))  #criando uma tabla para aguardar os valores
#         # OPERACIONES
# 
#        
#         for i in range(len(ats_global)): #
#             
#             for j in range(i+1,len(ats_global)): 
#                 distX = ((ats_global[i][0]) - (ats_global[j][0]))**2
#                 distY = ((ats_global[i][1]) - (ats_global[j][1]))**2
#                 distZ = (ats_global[i][2] - ats_global[j][2])**2
#                 
#                 
#                 distEu = ((distX + distY + distZ) ** (1/2))
#                 distancias [i,j] = distEu
#                
#         distanciasAbajo = distancias.T  
#         distFinal = distancias + distanciasAbajo
#         
#         print("\t MENU \n 1 - Cambiar de proteﾃｭa \n 2 - ﾃ》omos a menos de d Angstroms de un dado\
#         \n 3 - Distancias por debajo de un umbral \n 4 - TERMINAR")    
#         opc = int(input("Cual es la opcion? "))
#      
#     elif (opc == 2):
#         
#           
#             ##  2. ﾃ》omos a menos de d Angstroms de uno dado'     
#         # =============================================================================
#         print(distFinal)
#         maximo = distFinal.max()
#         minimo = maximo
#         for a in distFinal: # calcular o minimo percorrendo tudo
#              for b in a:
#                 if (b < minimo) and (b != 0):
#                      minimo = b                
#          
#         print ("la distancia minima es {} y la maxima es {}".format(minimo, maximo))
#          
#         cercanos = [] # guardar el indice del punto menor
#         protag = int(input("Cual es el punto de la matriz que queires comparar?"))
#         umbralDist =  float(input("Cual es el umbral?"))
#         infors = []
#          
#         for k in range(len(distancias)):
#             
#             if (distFinal[protag][k] < umbralDist) and  (protag != k):
#                 
#                 cercanos.append(k)
#          
#         for c in cercanos:
#             
#             
#             print(ats_info[c])
#          
#         print("\t MENU \n 1 - Cambiar de proteﾃｭa \n 2 - ﾃ》omos a menos de d Angstroms de un dado\
#         \n 3 - Distancias por debajo de un umbral \n 4 - TERMINAR")    
#         opc = int(input("Cual es la opcion? "))      
#     # =============================================================================
# 
#       ## 3. Distancias por debajo de un umbral'
#       
#       
#     elif (opc == 3):
#         
#         maximo = distFinal.max()
#         minimo = maximo
#         for a in distFinal: # calcular o minimo percorrendo tudo
#             for b in a:
#                 if (b < minimo) and (b != 0):
#                     minimo = b
#                 
#         
#         print ("la distancia minima es {} y la maxima es {}".format(minimo, maximo))
#         listita= [] # guardar el indice del punto menor
#         
#         umbralDist =  float(input("Cual es el umbral? "))
#         print("3' \t     5' \n ")
#         for w in range(len(distFinal)):
#             for k in range(w+1,len(distFinal)) :
#                 if (distFinal[w][k] < umbralDist):        
#                     listita.append([w, k])
#                     print("{} \t  \t {}".format(w,k))
#         
#        
#         
#         print("\t MENU \n 1 - Cambiar de proteﾃｭa \n 2 - ﾃ》omos a menos de d Angstroms de un dado\
#         \n 3 - Distancias por debajo de un umbral \n 4 - TERMINAR")    
#         opc = int(input("Cual es la opcion? "))
# =============================================================================

    if (opc == 4):
        fig = plt.figure(figsize = (8,8), dpi = 175, frameon = False)
        ax = fig.add_subplot(projection='3d') 
        atGl = np.array(ats_global)
        atChains = []
        for w in range(0,len(ats_chains)):
            atChains.append(np.array(ats_chains[w]))
       
       
        
        min_x = np.min(atGl[:,0])
        max_x = np.max(atGl[:,0])
        min_y = np.min(atGl[:,1])
        max_y = np.max(atGl[:,1])
        min_z = np.min(atGl[:,2])
        max_z = np.max(atGl[:,2])
        ax.set_xlim(min_x, max_x)
        ax.set_ylim(min_y, max_y)
        ax.set_zlim(min_z, max_z)
        #ax.set_xlim(-50, 50)
        #ax.set_ylim(-50, 50)
        #ax.set_zlim(-50, 50)
        
        edcol = 'brgmykcbrgmykcbrgmykc'
        col = 'kkkkkkkwwwwwwwmmmymmm'
        i = 0 #para ir cambiando el color de cada cadena
        for k in atChains:
            x = k[:,0]
            y = k[:,1]
            z = k[:,2]
            ax.scatter3D(x, y, z, c=col[i], edgecolors=edcol[i],
            marker='o', s=5, depthshade=False)
            i += 1 #i = i + 1
        
        plt.show()

         
        print("\t MENU \n 1 - Cambiar de proteﾃｭa \n 2 - ﾃ》omos a menos de d Angstroms de un dado\
\n 3 - Distancias por debajo de un umbral \n 4 - TERMINAR")    

        opc = int(input("Cual es la opcion? "))

print("HASTA LUEGO!!")

