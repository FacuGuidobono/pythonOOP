'''
+--------------------------------------------------------------------------------+
|                                 Ejercicio 7                                    |
|                                                                                |
|                   CONVERTIR A COMPRESION UNA ITERACION                         |
|                                                                                |
+--------------------------------------------------------------------------------+


'''
from modulos.decorators import *


def main():
    clear_console()

    print_box(                    'CONVERTIR A COMPRESION UNA ITERACION'                  ,'blue')

    printc('''Dada la siguiente iteración:
    cubos = [ ]
    for x in range (10) :
        cubos . append (x ∗∗ 3)
    convertirla en comprensión. ''','green')

    printc('-'*150,'magenta')
    printc('cubos = [x**3 for x in range(10)]','yellow')
    printc('-'*150,'magenta')
    
    printc('-'*150,'magenta')
    printc(f'cubos = {[x**3 for x in range(10)]}','yellow')
    printc('-'*150,'magenta')
    
    
if __name__ == '__main__':
    main()