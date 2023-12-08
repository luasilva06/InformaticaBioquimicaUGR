'''Implemente un programa que pida al usuario tres letras (indicando para cada
lectura que losposibles valores son A, U, G o C), y que identifique
 (muestre por pantalla) qué aminoácido se correspondería con dicha secuencia. 
 Para ello tenga en cuenta la siguiente tabla:'''
 
 # INICIALIZACION
base1 = input("Cual la primera base? A, U, G o C ->   ")
base2 = input("Cual la segunda base? A, U, G o C ->   ")
base3 = input("Cual la tercera base? A, U, G o C ->   ")
AA = base1 + " " + base2 + " " + base3

# OPERACIONES & SALIDAS
if (base1 == "U"):
    if ( base2 == "U") and ( (base3 == "U") or (base3 == "C") ):
        print(" El aminoacido es Fenilalanina - {}". format(AA))
    elif ( base2 == "U") and ( (base3 == "A") or (base3 == "G") ):
        print(" El aminoacido es leucina - {}". format(AA)) 
    elif (base2 == "C"):
         print(" El aminoacido es Serina - {}". format(AA))
    elif (base2 == "A"):
        if ( (base3 == "U") or (base3 == "C")):
            print(" El aminoacido es tirosina - {}". format(AA))
        else: print(print(" El aminoacido es 'paro ' - {}". format(AA)))
    elif (base2 == "G"):
        if (base3 == "U") or (base3 == "C"):
            print(" El aminoacido es Cisteína - {}". format(AA))
        elif (base3 == "A"):
            print(" El aminoacido es 'paro' - {}". format(AA))
        else: print(" El aminoacido es Triptofano - {}". format(AA))
elif (base1 == "C"):
    if (base2 == "U"):
        print(" El aminoacido es leucina - {}". format(AA))
    elif ( base2 == "C"):
        print(" El aminoacido es Prolina - {}". format(AA))
    elif (base2 == "A"):
        if ((base3 == "U") or (base3 == "C")):
            print(" El aminoacido es Histidina - {}". format(AA))
        else: print(" El aminoacido es Glutamina - {}". format(AA))
    else: print(" El aminoacido es Arginina - {}". format(AA))
elif (base1 == "A"):
    if (base2 == "U"):
        if (base3 == "U") or (base3 == "C"):
            print(" El aminoacido es Isoleucina - {}". format(AA))
        elif (base3== "A") or (base3 == "G"):
              print(" El aminoacido es Metionina - {}". format(AA))
    elif (base2 == "C"):
        if (base3 == "U") or (base3 == "C"):
            print(" El aminoacido es Treonina - {}". format(AA))
        else: print(" El aminoacido es Lisina - {}". format(AA))
    elif (base2 == "A"):
        if (base3 == "U") or (base3 == "C"):
            print(" El aminoacido es Asparagina - {}". format(AA))
        else: print(" El aminoacido es Arginina - {}". format(AA))
    elif (base2 == "G"):
        if (base3 == "U") or (base3 == "C"):
            print(" El aminoacido es Serina - {}". format(AA))
        else: print(" El aminoacido es Arginina - {}". format(AA))
elif (base1 == "G"):
    if (base2 == "U"):
        print(" El aminoacido es Valina - {}". format(AA))
    elif (base2 == "C"): 
        print(" El aminoacido es Alanina - {}". format(AA))
    elif (base2 == "A"):
        if (base3 == "U") or (base3 == "C"):
            print(" El aminoacido es Ácido aspárico - {}". format(AA))
        else: print(" El aminoacido es Ácido glutámico - {}". format(AA))
    else: print(" El aminoacido es Glicina - {}". format(AA))
else: print ("Aminoacidos invalidos!")
