'''Escriba un script que pida una distancia en milímetros y muestre su equivalente en metros,
centímetros y milímetros. Ejemplo: 1033 milímetros serían equivalentes a 1 metro, 3
centímetros y 3 milímetros.'''

# INICIALIZACION

distMm= int(input("Digite la distancia em milímetros: "))

# OPERACIONES

distMt=distMm//1000
distCm=(distMm%1000)//10
distMil=(distMm%1000)%10


# SALIDAS

print("{} milímetros serían equivalentes a {} metro, {} centímetros y {} milímetros.". format(distMm,distMt,distCm,distMil))

