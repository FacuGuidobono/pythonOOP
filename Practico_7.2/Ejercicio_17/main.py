'''
+--------------------------------------------------------------------------------+
|                                Ejercicio 17                                    |
|                                                                                |
|                              funciones lambda                                  |
|                                                                                |
|                                                                                |
+--------------------------------------------------------------------------------+


'''
from modulos.decorators import *
from modulos.lambdas import select_function as sf
from modulos.funciones import funciones as f
    
def main():
    
    title = ['Calcular el doble de un número', 
         'Determinar si un número es impar', 
         'Dados dos strings retornar el de mayor longitud',
         'Dada una dupla retornar otra cuya primera componente sea el doble de la primer componente de la dupla de entrada y el segundo ítem sea el triple del segundo ítem de la dupla de entrada',
         'Determinar si un número es mayor que 0',
         'Determinar si un número está dentro de un rango determinado',
         'Determinar si un punto está dentro de una circunsferencia',
         'Calcular el área de un triángulo rectangulo',
         'Calcular el área de un cuadrado',
         'Ordenar de forma ascendente o descendente una lista de números enteros',
         ]


    id = menu_principal(title)
    funct = sf(id)
    return f(id, funct)
    
            
if __name__ == '__main__':
    continuar = True  

    while continuar:
        continuar = main()
    