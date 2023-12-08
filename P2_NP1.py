'''Consulte los valores predefinidos para el máximo, mínimo, etc., valor real representable en su
sistema para Python.'''
import sys
print("valor maximo para el sistema de 64bits: {}".format(sys.maxsize))
print("valores maximo de valor real: {} \n minimo {} \n expoente maximo {}"
      "\n expoente minimo {}".format(sys.float_info.max,sys.float_info.min,
    sys.float_info.max_exp,sys.float_info.min_exp)
    )

