'''Dados los escalares a = 5, b = 2, c = -4, determinar los valores de verdad de las proposiciones.'''

# INICIALIZACION
a=5
b=2
c=-4

# OPERACIONES
itemA= a>b
itemB= not (b<c)
itemC= (a>b) or (c>b)
itemD= not ((a<b) and (c<b))
itemE= (a < b and a > c) or (b > c)
itemF= (a >= b and b <= c) or (a > c)
itemG= ((a > b) or (a > c))
itemH= (a > b) or ((a > c) and (b < a))
itemI= (a < b and a > c) or (b > c)

# SALIDAS
print("Resultados: \n\t A={} \n\t B={} \n\t C={} \n\t D={} \n\t E={} "
      "\n\t F={} \n\t G={} \n\t H={} \n\t I={}".format(itemA,itemB,itemC,itemD,itemE,itemF,
                                                       itemG,itemH, itemI))