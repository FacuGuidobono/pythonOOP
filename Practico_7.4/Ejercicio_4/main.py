'''
+====================================================================================+
|                                                                                    |
|  ordenar una lista de duplas por el primer ítem (nombre) o el segundo ítem (edad)  |          
|                                                                                    |
+====================================================================================+    '''
from decorators import *

def ordenar_por_edad(lista):
    return sorted(lista, key=lambda x: x[1])

def ordenar_por_nombre(lista):
    return sorted(lista, key=lambda x: x[0])

def main():
    clear_console()
    lista = [('Facundo', 25), ('Sol', 30), ('Camila', 22), ('David', 28), ('Josefina',30)]
    x_nombre = ordenar_por_nombre(lista)
    x_edad = ordenar_por_edad(lista)
    
    print_box('Ordenar una lista de duplas por el primer ítem (nombre) o el segundo ítem (edad)'.center(120),'green')
    
    printc('ORDENADA POR NOMBRE: \n' ,'red')
    printc(x_nombre,'red')
    printc('-'*124,'magenta',style='bold')
    
    printc('ORDENADA POR EDAD: \n','yellow')
    printc(x_edad,'yellow')
    printc('-'*124,'magenta',style='bold')

if __name__ == '__main__':
    main()