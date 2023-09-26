'''
+--------------------------------------------------------------------------------+
|                                Ejercicio 29                                    |
|                                                                                |
|                               Contador Modulo                                  |
|                                                                                |
|                                                                                |
+--------------------------------------------------------------------------------+


'''
from clases.contador import ContadorModulo
from modulos.decorators import *



def main():
    print_box('                 CONTADOR MODULO                 ','green')

    modulo  = int(input('Ingrese el modulo del contador: '))

    contador = ContadorModulo(modulo)

    i = iter(contador)
    printc('-'*53 , 'magenta')

    for _ in  range(modulo*2): # contamos 2 veces el modulo del contador para ver como se reincia
         printc(f'CONTANDO: {i.next()}', 'yellow')
         printc('-'*53 , 'magenta')
    
    msg_continuar()

if __name__ == '__main__':
     main()
