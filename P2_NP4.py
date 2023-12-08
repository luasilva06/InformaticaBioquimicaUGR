'''Escriba un script que pida al usuario un valor de temperatura C en grados celsius y muestre las
equivalencias a grados Farenheit, Kelvin y Reamur:
F = 9/5 (C−32)      K = C + 273,15          R = 8/10 C'''

## PROFESSOR, LA FORMULA PARA °C PARA °F ES (F=C*1,8+32)


# INICIALIZACION
cel= float(input("Qual la temperatura en °C?"))

# OPERACIONES

far = (9/5) *cel + 32
kel = cel + 273.15
rea= (8/10) * cel

# SALIDAS

print("{} °C es {} °F, {} K e {}°R".format(cel,far,kel,rea))