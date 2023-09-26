'''
+--------------------------------------------------------------------------------+
|                                 Ejercicio 2                                    |
|                                                                                |
|      Escriba una lista que permita generar una lista de potenciasde dos.       |
|                                                                                |
|                                                                                |
+--------------------------------------------------------------------------------+


'''

from modulos.decorators import *


def main():
    
    print_box('                         LISTA DE POTENCIAS DE DOS                        ','red')
    
    try:
        num = int(input('Ingrese el numero de potencias de dos que desea generar: '))
        pot_dos = [2 ** i for i in range(num)]
    except ValueError:
      msg_error()
      
    printc('-'*150,'magenta')
    printc(f'Lista de potencias de dos: {pot_dos}', 'green')
    printc('-'*150,'magenta')
    msg_continuar()
    

if __name__ == '__main__':
    main()
