from modulos.decorators import menu_principal,msg_error



def select_function(id : int = 0) -> callable:
    if id == 1:
        return lambda x : x * 2  # doble
    elif id == 2:
        return lambda x : x % 2 != 0 # impar
    elif id == 3:
        return lambda x, y : x if len(x) > len(y) else y # string mayor
    elif id == 4:
        return lambda x, y : (x * 2, y * 3) # tupla
    elif id == 5:
        return lambda x : x > 0 # positivo
    elif id == 6:
        return lambda x, y : x >= y[0] and x <= y[1] # rango
    elif id == 7:
        return lambda x_centro , y_centro, x_punto, y_punto, radio : (x_centro - x_punto)**2 + (y_centro - y_punto)**2 <= radio**2 # punto dentro de circunferencia
    elif id == 8:
        return lambda b,h : b* h / 2 #area triangulo
    elif id == 9:
        return lambda x : x * x # area cuadrado
    elif id == 10: 
            a = menu_principal(['Ordenar forma ascendente', 'Ordenar forma descendente'])
            if a == 1:
                return lambda x : sorted(x) #ordenar de forma ascendente o descendente 
            elif a == 2:
                return lambda x : sorted(x, reverse = True)
            else:
                msg_error()
    elif id == 0:
        return False     
    