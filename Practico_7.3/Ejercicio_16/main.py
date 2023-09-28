'''
+--------------------------------------------------------------------------------+
|                                 Ejercicio 16                                   |
|                                                                                |
|             Generador de divisores de un número ingresado por el usuario       |
|                                                                                |
|                                                                                |
+--------------------------------------------------------------------------------+

'''



from modulos.decorators import *

def generador_divisores(num):
    i = 1

    while True:
        if num % i == 0:
            yield i   
        i += 1

    
        
def main():
    clear_console()
    print_box('         GENERADOR DE DIVISORES        ','magenta')
    
    num = validacion_un_numero('Ingrese un numero para obtener sus divisores: ', int)
    
    generador = generador_divisores(num)
    
    lista = []

    for _ in range(num):
        divisor = next(generador)
        lista.append(divisor)
        if divisor == num:
            break

    printc('-'*100,'green',style='bold')
    printc(f'Divisor/es: {lista}','yellow')
    printc('-'*100,'green',style='bold')
    print('\n')
                
        
        
        
                



if __name__ == '__main__':
    main()  
