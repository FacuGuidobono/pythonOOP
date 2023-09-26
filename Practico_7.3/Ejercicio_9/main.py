'''
+--------------------------------------------------------------------------------+
|                                 Ejercicio 9                                    |
|                                                                                |
|           diccionario cuya clave sea  un número natural y cuyo valor           |
|              sea la tabla de multiplicar correspondiente a la clave.           |
|                                                                                |
+--------------------------------------------------------------------------------+


'''
from modulos.decorators import *


def generar_tablas_multiplicar(n):
    
    tabla = {}
    for i in range(1, n + 1):
        tabla[i] = [i * j for j in range(1, 11)]  # Calcula la tabla de multiplicar para cada número

    return tabla

def main():
    
    clear_console()
    print_box('diccionario que contenga tablas de multiplicar'.upper(),'green')

    n = 10  # Puedes ajustar este valor para obtener más tablas de multiplicar
    tablas = generar_tablas_multiplicar(n)
    printc('-'*150,'magenta')
    for clave, valor in tablas.items():
         print(f"Tabla de multiplicar del {clave}: {valor}")
         printc('-'*150,'magenta')


if __name__ == '__main__':
    main()