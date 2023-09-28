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
    
    cantidad_de_palindromos = 200
    
    generador = generador_palindromos()
    lista = []
    for _ in range(cantidad_de_palindromos):
        if _ >= 9:
            palindromo = next(generador)
            lista.append(palindromo)
            
            if _ % 9 == 0:
                printc('-'*100,'green')
                palindromo = next(generador)
                printc(f'Palindromos: {lista}','yellow')
                printc('-'*100,'green')
                print('\n')
                lista = []
                



if __name__ == '__main__':
    main()  


