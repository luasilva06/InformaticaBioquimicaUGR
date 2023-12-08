'''Escriba un script que pida las coordenadas de dos puntos en el plano, (x1, y1), (x2, y2), y
calcule los coeficientes (a, b, c) de la ecuación general de la recta ax+by+c=0 que los une. El
cálculo de los coeficientes se realiza mediante las expresiones: a=y2−y1, b=x1−x2,c=y1 x2−y2 x1.
Muestre el resultado en la forma ax+by+c=0 utilizando los valores
calculados.'''

# INICIALIZACION
x1= float(input("Qual el valor de X1?"))
x2= float(input("Qual el valor de X2?"))
y1= float(input("Qual el valor de Y1?"))
y2= float(input("Qual el valor de Y2?"))

# OPERACIONES

a= y2 - y1
b= x1 - x2
c= y1 * x2 - y2 * x1

# SALIDAS

print(" La ecuacion es {}x + {}y + {}".format(a,b,c))
