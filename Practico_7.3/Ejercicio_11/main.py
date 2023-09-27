'''
+--------------------------------------------------------------------------------+
|                                 Ejercicio 11                                   |
|                                                                                |
|                        Generador de palíndromos numéricos                      |
|                                                                                |
|                                                                                |
+--------------------------------------------------------------------------------+

'''

from modulos.decorators import *

def generador_palindromos():
    n = 0
    while True:
        n_str = str(n)
        if n_str == n_str[::-1]:
            yield n
        n += 1
        
        
def main():
    print_box('         GENERADOR DE PALINDROMOS NUMERICOS         ','magenta')
    # Ejemplo de uso del generador para obtener los primeros 10 palíndromos
    generador = generador_palindromos()
    for _ in range(10):
        palindromo = next(generador)
        print(palindromo)
        


if __name__ == '__main__':
    main()  


