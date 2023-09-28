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
    for i in range(1, num + 1):
        if num % i == 0:
            yield i
        
        
def main():
    clear_console()
    print_box('         GENERADOR DE DIVISORES        ','magenta')
    
    num = validacion_un_numero('Ingrese un numero para obtener sus diviores: ', int)
    
    generador = generador_divisores(num)
    
    
    for divisor in generador:
       
        printc('-'*100,'green',style='bold')
        printc(f'Multiplo/s: {divisor}','yellow')
        printc('-'*100,'green',style='bold')
        print('\n')
                
        
        
        
                



if __name__ == '__main__':
    main()  
