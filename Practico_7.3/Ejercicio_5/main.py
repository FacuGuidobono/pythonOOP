'''
+--------------------------------------------------------------------------------+
|                                 Ejercicio 5                                    |
|                                                                                |
|     eliminar de una lista de números enteros positivos los números pares.      |
|                                                                                |
|                                                                                |
+--------------------------------------------------------------------------------+


'''
import random
from modulos.decorators import *

def main():
    
    print_box(              'eliminar de una lista de números enteros positivos los números pares.'.upper(),                'green'     )

    numeros = [random.randint(1, 40) for _ in range(10)] #lista de numeros enteros > 0 randoms

    numeros_impares = [x for x in numeros if x % 2 != 0]  #numeros imperas de la lista de numeros
    
    printc('-'*150,'magenta')
    printc(f'Lista Original: {sorted(numeros)}','yellow')
    printc('-'*150,'magenta')
    printc(f'Lista de Numeros Impares: {sorted(numeros_impares)}','green')
    printc('-'*150,'magenta')
    msg_continuar()
    
if __name__ == '__main__':
    main()