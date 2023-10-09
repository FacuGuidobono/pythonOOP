'''
+====================================================================================+
|                                                                                    |
|      Se Resuelven distintos tipos de Ejercicios con Funciones De Orden Superior    |          
|                                                                                    |
+====================================================================================+    '''



from functools import reduce
from decorators import *

# Definir las listas
paises  = ['Estonia', 'Finlandia', 'Suiza', 'Dinamarca', 'Noruega', 'Islandia']
nombres = ['Carlos', 'Daniel', 'Alberto', 'Luis']
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ejemplo = [1, 'a', 'b', 2, 'c']
paises_norte = ['Estonia', 'Finlandia', 'Dinamarca', 'Noruega', 'Islandia']
todo = [paises, nombres, numeros, ejemplo, paises_norte]



#<------------------------------------------------------------------------>
def recuperarString(lista):
    return list(filter(lambda x: isinstance(x, str), lista))
#<------------------------------------------------------------------------>

def main():
    clear_console()
    #<------------------------------------------------------------------------>

    title = 'DATOS ORIGINALES'
    print_box(title.center(120),'red')

    #<------------------------------------------------------------------------>
    for elemento in todo:
        print(elemento)
        printc('-'*124,'magenta')

    #<------------------------------------------------------------------------>
    paises_mayusculas = list(map(str.upper, paises))
    números_cuadrados = list(map(lambda x: x**2, numeros))
    nombres_mayusculas = list(map(str.upper, nombres))
    paises_con_n = list(filter(lambda pais: 'n' in pais.lower(), paises))
    paises_mas_de_seis = list(filter(lambda pais: len(pais) > 6, paises))
    paises_con_e = list(filter(lambda país: 'e' in país.lower(), paises))
    suma_numeros = reduce(lambda x, y: x + y, numeros)
    paises_norte_juntos = reduce(lambda x, y: x + ", " + y, paises_norte)
    #<------------------------------------------------------------------------>
    
    print_box("Países en mayúsculas".center(120), 'red')
    print(paises_mayusculas)

    print_box("Cuadrados de los números".center(120), 'red')
    print(números_cuadrados)

    print_box("Nombres en mayúsculas".center(120), 'red')
    print(nombres_mayusculas)

    print_box("Países con 'n'".center(120), 'red')
    print(paises_con_n)

    print_box("Países con más de seis caracteres".center(120), 'red')
    print(paises_mas_de_seis)
    
    print_box("Países con 'e'".center(120),'red')
    print(paises_con_e)

    print_box("Lista de strings".center(120),'red')
    print(recuperarString(ejemplo))
    
    print_box("Suma de números".center(120), 'red')
    print(suma_numeros)

    print_box('Paises del norte de Europa'.center(120), 'red')
    print(paises_norte_juntos + '\n')
    #<------------------------------------------------------------------------>


if __name__ == '__main__':
    main()
 