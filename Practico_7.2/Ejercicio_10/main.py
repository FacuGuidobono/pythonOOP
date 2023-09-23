'''
+--------------------------------------------------------------+
|                                                              |
|   Ejercicio 10 - Eliminar ultimos n elementos de una lista   |
|                                                              |
+--------------------------------------------------------------+


'''

from modulos.decorators import *

def butlast(n: int = 0, l: list = None) -> list:

    if n <= 0:
        printc("No se realizaron cambios en la lista, ingrese un valor distinto\n","red")
        msg_continuar()
        return l

    return list(filter(lambda i: i < len(l) - (n) , l))

def main():
    # Ejemplo de uso:
    print_box("     ELIMINANDO ULTIMOS n ELEMENTOS DE UNA LISTA     ",'green')
    lista = [1,2,3,4,5,6,7,8,9,10,11,12]
    printc(f'\nLista original: {lista}\n','yellow')

    try:
        
        n = int(input(f'Ingrese un numero entre 1 y {len(lista)} para eliminar los ultimos items de la lista:'))
    except ValueError:
        msg_error()
        msg_continuar()
    
    mod_lista =butlast(n,lista)
    printc(f'Lista modificada: {mod_lista}','green')
    msg_continuar()
    
if __name__ == '__main__':
    main()
   