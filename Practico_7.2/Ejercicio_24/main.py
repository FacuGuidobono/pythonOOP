'''
+--------------------------------------------------------------------------------+
|                                Ejercicio 24                                    |
|                                                                                |
|                          Area Triangulo/Rectangulo                             |
|                                                                                |
|                                                                                |
+--------------------------------------------------------------------------------+


'''

from modulos.decorators import *



def main():

    generarÁrea = lambda tipo_de_area, base, altura: (0.5 * base * altura) if tipo_de_area else (base * altura)
    id = menu_principal(['Generar area de triangulo', 'Generar area de rectangulo'])

    if id == 1:

        tipo_de_area = True
        title = 'Area de triangulo'
             
         

    elif id == 2:
        tipo_de_area = False
        title = 'Area de rectangulo'
    
    elif id == 0:
        return False
    
    else:
        msg_error()
        msg_continuar()
    

    try:    
            print_box(f'{title}','red')
            base = float(input('ingrese la base (cm): '))
            altura = float(input('ingrese la altura (cm): '))
            clear_console()
            print_box(f'{title}','red')
            printc(f'Base: {base}','yellow')
            printc(f'Base: {altura}','yellow')
            printc(f'{title}: {generarÁrea(tipo_de_area, base, altura)}','green')
            msg_continuar()
            return True

    except ValueError:
            msg_error()
            msg_continuar()
            
   

   


if __name__ == '__main__':
   continuar = True

   while continuar: 
    
        continuar = main()
    