'''
+--------------------------------------------------------------------------------+
|                                Ejercicio 15                                    |
|                                                                                |
|        función lambda que reciba como parámetro dos números enteros            |
| y retorne como resultado el mayor o, en caso de igualdad, el primer argumento. |
|                                                                                |
+--------------------------------------------------------------------------------+


'''
from modulos.decorators import *


def main():
    
    title = 'función lambda que recibe como parámetro dos números enteros y retorne como resultado el mayor o, en caso de igualdad, el primer argumento.'
    print_box(f"{title}",'green')
    f = lambda x,y: y if y > x else x
    try: 
        x = int(input('Ingrese un numero entero: '))
        y = int(input('Ingrese otro numero entero: '))
    
    except ValueError:
        msg_error()
        return
    
    printc(f'El mayor es: {f(x,y)}','green')
    msg_continuar()

if __name__ == '__main__':
    main()  