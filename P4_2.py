import Bio.PDB as pdb


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
        for residue in chain:
            for atom in residue:
               ats_global.append(list(atom.get_coord()))
            ats_info.append([atom.get_name(),atom.get_id()])
        ats_chains.append([ats_global])

print("\n--\n" * 3)
print(ats_global)
print("\n--\n" * 3)
print(ats_info)
print("\n--\n" * 3)
print(ats_chains)

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
            for residue in chain:
                for atom in residue:
                   ats_global.append(list(atom.get_coord()))
                ats_info.append([atom.get_name(),atom.get_id()])
            ats_chains.append([ats_global])
    
    print("\n--\n" * 3)
    print(ats_global)
    print("\n--\n" * 3)
    print(ats_info)
    print("\n--\n" * 3)
    print(ats_chains)
    
    print("      MENU \n 1 - Cambiar de proteina \n 2 - TERMINAR")
    opc = int(input("Cual es la opcion? "))


if opc == 2:
    print("HASTA LUEGO!")

else:
    print("\n Opcion invalida \n")
    print("      MENU \n 1 - Cambiar de proteina \n 2 - TERMINAR")
    opc = int(input("Cual es la opcion? "))