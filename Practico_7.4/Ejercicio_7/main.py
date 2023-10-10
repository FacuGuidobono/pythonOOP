'''
+====================================================================================+
|                                                                                    |
|     Suma los elementos de l que cumplen con la condición establecida por f.        |          
|                                                                                    |
+====================================================================================+    '''

from decorators import *


def crearPotencia(exponente):
  return lambda numero: numero ** exponente


def main():

    print_box('Potencias de 2 al 11 del N°2'.center(120),'red')
    potencias = [crearPotencia(i) for i in range(2,11)]  #creamos una lista que contiene las funciones que crean las potencias del 2 al 11
    
    printc('-'*124,'magenta',style='bold')
    i=2
    for potencia in potencias:  
      
        printc(f'Potencia {str(i).center(3)} del N°2: {str(potencia(2)).center(130)}')  #imprimimos todas las potencias del numero dos creadas anteriormente
        printc('-'*124,'magenta',style='bold')
        i+=1

if __name__ == "__main__":
    main()

