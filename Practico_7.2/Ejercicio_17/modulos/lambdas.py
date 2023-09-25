from modulos.decorators import menu_principal



def select_function(id : int = 0) -> callable:
    if id == 1:
        return lambda x : x * 2
    elif id == 2:
        return lambda x : x % 2 != 0
    elif id == 3:
        return lambda x, y : x if len(x) > len(y) else y
    elif id == 4:
        return lambda x, y : (x * 2, y * 3)
    elif id == 5:
        return lambda x : x > 0
    elif id == 6:
        return lambda x, y : x >= y[0] and x <= y[1]
    elif id == 7:
        return lambda x, y, z : (x - y) ** 2 + (z - y) ** 2 <= y ** 2
    elif id == 8:
        return lambda b,h : b* h / 2
    elif id == 9:
        return lambda x : x * x 
    elif id == 10:
            a = menu_principal(['Ordenar forma ascendente', 'Ordenar forma descendente'])
            if a == 1:
                return lambda x : sorted(x)
            else:
                return lambda x : sorted(x, reverse = True)
    elif id == 0:
        return False     
    