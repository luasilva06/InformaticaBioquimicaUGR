'''Incluya el c√≥digo necesario sobre el ejercicio anterior para que se calcule
la matriz de distancias a partir de las posiciones x,y,z almacenadas en la 
matriz ats_global (es decir, a partir de la matriz que contiene todas las 
coordenadas), cada vez que se lea una nueva prote√≠na mediante la opci√≥n'''

import Bio.PDB as pdb
import numpy as np


print("/t MENU \n 1 - Elegir una de proteina \n 2 - Calcular las distancias atomicas \
\n 3 - TERMINAR")
opc = int(input("Cual es la opcion? "))
while opc != 3 :
    if opc == 1:
        fichero = input("Nombre del fichero de la proteÌna (sin extensiÛn): ")
        fichero += '.pdb'
        parser = pdb.PDBParser()
        try:
            s = parser.get_structure('my_pdb', fichero)
        except:
            s = parser.get_structure('my_pdb', '1clg.pdb') #fichero por defecto
        
        print("CABECERA")
        print(s.header)
        print("\n\nNOMBRE DE LA PROTEÕNA:")
        print(s.header['head'])
        print("\n\nKEYWORDS:")
        print(s.header['keywords'])
        print("\n\nCADENAS QUE CONTIENE:")
        print(s.header['compound']['1']['chain'])
        
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
        
        print("\n--\n" * 3)
        print(ats_global)
        print("\n--\n" * 3)
        print(ats_info)
        print("\n--\n" * 3)
        print(ats_chains)
        
        print(" /t MENU \n 1 - Elegir una de proteina \n 2 - Calcular las \
distancias atomicas \n 3 - TERMINAR")
        opc = int(input("Cual es la opcion? "))


    elif opc == 2:
        fichero = input("Nombre del fichero de la protei≠na (sin extension): ")
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
                for residue in chain:
                    for atom in residue:
                       ats_global.append(list(atom.get_coord()))
                    ats_info.append([atom.get_name(),atom.get_id()])
                ats_chains.append([ats_global])

        #num_ats = len(ats_global)
        distancias = np.zeros ((len(ats_global),len(ats_global)))  #criando uma tabla para aguardar os valores
        # OPERACIONES

        # D = (((x1-x2)**2) + ((y1-y2)**2) + ((Z1 - Z2)**2)) ** 1/2
        for i in range(len(ats_global)): # correu os valores macro
            
            for j in range(i+1,len(ats_global)): # correr os micro e a uma posi√ß√£o a mais, para n√£o repetir
                distX = ((ats_global[i][0]) - (ats_global[j][0]))**2
                distY = ((ats_global[i][1]) - (ats_global[j][1]))**2
                distZ = (ats_global[i][2] - ats_global[j][2])**2
                
                
                distEu = ((distX + distY + distZ) ** (1/2))
                distancias [i,j] = distEu
                #print("La distancia entre los puntos {} y {} es {:.2f}".format(puntos[i][i],puntos[j][i],distEu))
        distanciasAbajo = distancias.T  
        distFinal = distancias + distanciasAbajo     
        #SALIDAS
               #print("La distancia entre los puntos es: {:.2f}".format(distEu))
             
        print(distFinal)
        print("/t MENU \n 1 - Elegir una de proteina \n 2 - Calcular las \
distancias atomicas \n 3 - TERMINAR")
        opc = int(input("Cual es la opcion? "))

    else:
        print("\n Opcion invalida \n")
        print("/t MENU \n 1 - Elegir una de proteina \n 2 - Calcular las \
distancias atomicas \n 3 - TERMINAR")
        opc = int(input("Cual es la opcion? "))
        
print("HASTA LUEGO!")