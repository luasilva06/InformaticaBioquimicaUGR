import math as mt
'''14. Escriba un script que pida las coordenadas de dos puntos en el plano, (x1, y1), (x2, y2), e
informe de la distancia euclídea entre ellos. Una vez mostrado el resultado debe pedir un
tercer punto (x3, y3) e informar del área del triángulo formado tomando dichos puntos
como vértices.
Pista: Usa la fórmula de Herón para calcular el área conocido el perímetro de un triángulo.'''

# INICIALIZACION

x1=int(input("Cual es el valor del x1? ->  "))
y1=int(input("Cual es el valor del y1? ->  "))
x2=int(input("Cual es el valor del x2? ->  "))
y2=int(input("Cual es el valor del y2? ->  "))

# OPERACIONES

dist12= ((x2 - x1) ** 2 + (y2 - y1) **2) **0.5

# SALIDA

print("La distancia de los puntos 1 e 2 es: {}.".format(dist12))

# 2ª PARTE - CONTINUACION

x3=int(input("Cual es el valor del x3? ->  "))
y3=int(input("Cual es el valor del y3? ->  "))

# 2ª PARTE - OPERACIONES
dist13= ((x3 - x1) ** 2 + (y3 - y1) **2) **0.5
dist23= ((x3 - x2) ** 2 + (y3 - y2) **2) **0.5
s=(dist12+dist13+dist23)/2
areaTri= (s*(s-dist12)*(s-dist13)*(s-dist23))**0.5

# 2ª PARTE - SALIDA

print("La area del triangulo es: {:.2f}".format(areaTri))

