from modulos.decorators import *


def funciones(id: int , funct: callable) -> bool:
    
        if id == 1:
            print_box("Calcular el Doble de un numero:",'green')
            try:
                num = int(input('Ingrese un numero: '))
                printc(f'\nResultado: {funct(num)}','yellow')
                msg_continuar()
                return True
            except ValueError:
                msg_error()
                
        elif id == 2:
            print_box("Determinar si un numero es impar:",'green')
            try:
                num = int(input('Ingrese un numero: '))
                printc(f'\nResultado: {funct(num)}','yellow')
                msg_continuar()
                return True
            except ValueError:
                msg_error()
                
        elif id == 3:
            print_box("Dados dos strings retornar el de mayor longitud:",'green')
            try:
                str1 = input('Ingrese el primer string: ')
                str2 = input('Ingrese el segundo string: ')
                printc(f'\nResultado: {funct(str1, str2)}','yellow')
                msg_continuar()
                return True
            except ValueError:
                msg_error()
        elif id == 4:
            print_box("Dada una tupla se duplica el 1er Argumento y Se triplica el 2do:",'green')
            try:
                x = float(input('Ingrese el primer numero: '))
                y = float(input('Ingrese el segundo numero: '))
                printc(f'\nResultado: {funct(x,y)}','yellow')
                msg_continuar()
                return True
            except ValueError:
                msg_error()
        elif id == 5:
            print_box("Comprobar si un numero es mayor que 0:",'green')
            try:
                num = float(input('Ingrese un numero: '))
                printc(f'\nResultado: {funct(num)}','yellow')
                msg_continuar()
                return True
            except ValueError:
                msg_error()
        elif id == 6:
            print_box("Comprobar si un numero esta dentro de un rango determinado:",'green')
            try:
                rango_min = float(input('Ingrese el rango minimo: '))
                rango_max = float(input('Ingrese el rango maximo: '))
                num = float(input('Ingrese el numero: '))
                printc(f'\nResultado: {funct(num, [rango_min, rango_max])}','yellow')
                msg_continuar()
                return True
            except ValueError:
                msg_error()
            
        elif id == 0:
            msg_salir()
            return False