'''10. Escriba un programa que calcule la velocidad de llenado de una piscina y el dinero que cuesta
llenarla. Pedirá el tiempo que tardó en llenarse en segundos, el total de litros consumidos y el
precio por litro. Debe informar de la velocidad de llenado en litro/segundo, de los litros/hora y
también del precio total.'''

# INICIALIZACION
tiempo = int(input("Cual fue el tiempo (segundos que tardó llenar la piscina?"))
litro= int(input("Total de litros consumidos?"))
euro= float(input("Cual es el precio por litro?"))

# OPERACIONES

velocidadeSeg= litro / tiempo
velocidadeHora=litro/(tiempo/3600)
precio = litro*euro

# SALIDAS

print("Litros\tTiempo\tEur/L\tL/sg\tL/hr\tprecio")
print("{} \t {} \t {} \t {} \t {} \t {:.2f} ".format(litro,tiempo,euro,velocidadeSeg,velocidadeHora,precio))