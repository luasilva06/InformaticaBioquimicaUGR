'''Realice un programa (script) que pida al usuario tres nÃºmeros y los muestre por pantalla de
manera ordenada.'''
# INICIALIZACION
num1=float(input("Introduza el 1º numero: "))
num2=float(input("Introduza el 2º numero: "))
num3=float(input("Introduza el 3º numero: "))

# OPERACIONES & SALIDAS
print("Los valores fueran n1 {} - n2 {} - n3 {} ".format(num1,num2,num3))
print("---------------------- ordenados -----------------")

if (num1 >= num2) and (num1 >= num3):  # x x 1
    if (num2 >= num3):    # x 2 1
        print(" 1º  {} -- 2º {} -- 3º {}".format(num3,num2,num1))
    elif (num2 <= num3): # 2 x 1
        print(" 1º  {} -- 2º {} -- 3º {}".format(num2,num3,num1))
elif (num2 >= num1) and (num2 >= num3): # x x 2
    if (num1 >= num3): # 3 1 2
        print(" 1º  {} -- 2º {} -- 3º {}".format(num3,num1,num2))
    elif ( num1 <= num3): # 1 3 2
        print(" 1º  {} -- 2º {} -- 3º {}".format(num1,num3,num2))
elif (num3 >= num1) and (num3 >= num2): # x x 3
    if (num1 >= num2): # 2 1 3
        print(" 1º  {} --  2º {} -- 3º {}".format(num2,num1,num3))
    elif (num1 <= num2): # 1 2 3
          print(" 1º  {} -- 2º {} -- 3º {}".format(num1,num2,num3))
else: print ("Numeros incorrectos")
              
        
         
