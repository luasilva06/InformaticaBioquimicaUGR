#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 

@author: carlos
"""
import Bio.PDB as pdb
import P5_1
import P5_2 



fichero = input("Nombre del fichero de la proteína (sin extensión): ")
fichero += '.pdb'
parser = pdb.PDBParser()
try:
    s = parser.get_structure('my_pdb', fichero)
except:
    s = parser.get_structure('my_pdb', '1clg.pdb') #fichero por defecto

print("CABECERA")
print(s.header)
print("\n\nNOMBRE DE LA PROTEÍNA:")
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
               cadena.append(list(atom.get_coord()))
               ats_info.append([atom.get_name(),atom.get_id()])
        ats_chains.append(cadena)


k = P5_1.matriz_distancias(ats_global)   
print("aquiiiii: {}".format(k))
P5_2.pinta_proteina(ats_chains, ats_global)

print("/t MENU \n 1 - Cambiar de proteina \n 2 - TERMINAR")
opc = int(input("Cual es la opcion? "))


while opc == 1 :
    
    fichero = input("Nombre del fichero de la proteína (sin extensión): ")
    fichero += '.pdb'
    parser = pdb.PDBParser()
    try:
        s = parser.get_structure('my_pdb', fichero)
    except:
        s = parser.get_structure('my_pdb', '1clg.pdb') #fichero por defecto
    
    '''print("CABECERA")
    print(s.header)
    print("\n\nNOMBRE DE LA PROTEÍNA:")
    print(s.header['head'])
    print("\n\nKEYWORDS:")
    print(s.header['keywords'])
    print("\n\nCADENAS QUE CONTIENE:")
    print(s.header['compound']['1']['chain'])
    '''
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
    
    k = P5_1.matriz_distancias(ats_global)   
    print("aquiiiiiiiiii",k)
    P5_2.pinta_proteina(ats_chains, ats_global)
    
    print("/t MENU \n 1 - Cambiar de proteina \n 2 - TERMINAR")
    opc = int(input("Cual es la opcion? "))