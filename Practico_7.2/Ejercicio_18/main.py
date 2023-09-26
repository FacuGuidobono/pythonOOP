
'''
+--------------------------------------------------------------------------------+
|                                Ejercicio 18                                    |
|                                                                                |
|                          Convertir Strings en Mayusculas                       |
|                                                                                |
|                                                                                |
+--------------------------------------------------------------------------------+


'''

from modulos.decorators import *




def f_mayusculas():                 
    return lambda texto: texto.upper()  # Define y devuelve una función lambda que convierte un string a mayúsculas






def main():

    id = menu_principal(['Convertir texto a mayusculas'])
    if id == 1:
        try:
            print_box('Texto Minusculas a Mayusculas','green')
            text = input('Ingrese un texto en minusculas para convertirlo a mayusculas: ')
            clear_console()
        except ValueError:
            msg_error()
    elif id == 0:
        return False
    
    else:
        msg_error()
    
    print_box('Texto Minuscula a Mayusculas','red')

    # Crear la función para convertir a mayúsculas
    text_a_mayusculas = f_mayusculas()

    
    resultado = text_a_mayusculas(text)
    printc('-'*50, 'magenta')
    printc(f'Texto Original: {text}', 'yellow')
    printc('-'*50, 'magenta')
    printc(f'Texto Convertido: {resultado}', 'green')
    printc('-'*50, 'magenta')
    msg_continuar()
    return True


if __name__ == '__main__':
    continuar = True
    while continuar:
        continuar = main()
