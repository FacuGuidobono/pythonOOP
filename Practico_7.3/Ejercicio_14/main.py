'''
+--------------------------------------------------------------------------------+
|                                 Ejercicio 14                                   |
|                                                                                |
|             Generador de múltiplos de un número ingresado por el usuario       |
|                                                                                |
|                                                                                |
+--------------------------------------------------------------------------------+

'''



from modulos.decorators import *
#------------------------------------------------------------------
def generador_multiplos(num):
    n = 1
    while True:
        yield n * num
        n += 1
        
#------------------------------------------------------------------       
def main():
    clear_console()
    print_box('         GENERADOR DE MULTIPLOS        ','magenta')
    
    num, cantidad = validacion_dos_numeros('Ingrese un numero para obtener sus multiplos: ', 'Ingrese la cantidad de multiplos que desea obtener: ', int)
    
    generador = generador_multiplos(num)
    lista = []
    
   
    for _ in range(cantidad):
        multiplo = next(generador)
        lista.append(multiplo)
    printc('-'*100,'green',style='bold')
    printc(f'Multiplo/s: {lista}','yellow')
    printc('-'*100,'green',style='bold')
    print('\n')
            
#------------------------------------------------------------------        

if __name__ == '__main__':
    main()  
