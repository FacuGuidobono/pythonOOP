'''
+====================================================================================+
|                                                                                    |
|     Suma los elementos de l que cumplen con la condición establecida por f.        |          
|                                                                                    |
+====================================================================================+    '''
from decorators import *


#---------------------------------------------------
def sumarSi(f, l):
  
  suma = 0
  for numero in l:
    if f(numero):
      suma += numero
  return suma

#---------------------------------------------------
def esPar(numero):
  return numero % 2 == 0


#<-------------------------------------------------------------------------------------

def main():

    numeros = [  validar_un_input(f"Ingrese un número : ", int) for _ in range(10)]

    sumarPares = sumarSi(esPar, numeros)

    print(sumarPares)
    
#<-------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()  
    
