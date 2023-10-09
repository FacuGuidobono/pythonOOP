from decorators import *

# Definir las listas
paises = ['Estonia', 'Finlandia', 'Suiza', 'Dinamarca', 'Noruega', 'Islandia']
nombres = ['Carlos', 'Daniel', 'Alberto', 'Luis']
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
title = 'DATOS ORIGINALES'
print_box(title.center(120),'red')

print(paises)
printc('-'*124,'magenta')
print(nombres)
printc('-'*124,'magenta')
print(numeros)
printc('-'*124,'red')
print('\n')
# 1. Usar la función map para crear una nueva lista con los nombres de países en mayúsculas.
paises_mayusculas = list(map(str.upper, paises))
print_box("Países en mayúsculas".center(120), 'yellow')
printc(paises_mayusculas, 'green')

# 2. Usar la función map para crear una nueva lista con el cuadrado de los números.
números_cuadrados = list(map(lambda x: x**2, numeros))
print_box("Cuadrados de los números".center(120), 'yellow')
printc(números_cuadrados, 'green')

# 3. Usar la función map para pasar a mayúsculas cada nombre en la lista de nombres.
nombres_mayusculas = list(map(str.upper, nombres))
print_box("Nombres en mayúsculas".center(120), 'yellow')
printc(nombres_mayusculas, 'green')

# 4. Usar la función filter para filtrar los países que contienen una 'n'.
paises_con_n = list(filter(lambda pais: 'n' in pais.lower(), paises))
print_box("Países con 'n'".center(120), 'yellow')
printc(paises_con_n, 'green')

# 5. Usar la función filter para filtrar los países con más de seis caracteres.
paises_mas_de_seis = list(filter(lambda pais: len(pais) > 6, paises))
print_box("Países con más de seis caracteres".center(120), 'yellow')
printc(paises_mas_de_seis, 'green')

# 6. Usar la función filter para filtrar los países que contienen la letra 'e'.
paises_con_e = list(filter(lambda país: 'e' in país.lower(), paises))
print_box("Países con 'e'".center(120), 'yellow')
printc(paises_con_e, 'green')

# 7. Definir la función recuperarString para obtener una lista con solo strings.
def recuperarString(lista):
    return list(filter(lambda x: isinstance(x, str), lista))
print_box("Lista de strings".center(120), 'yellow')
printc(recuperarString([1, 'a', 'b', 2, 'c']), 'green')

# 8. Usar reduce para sumar todos los números en la lista de números.
from functools import reduce
suma_numeros = reduce(lambda x, y: x + y, numeros)
print_box("Suma de números".center(120), 'yellow')
printc(suma_numeros, 'green')

# 9. Usar reduce para obtener un string que contenga todos los países del norte de Europa.
paises_norte = ['Estonia', 'Finlandia', 'Dinamarca', 'Noruega', 'Islandia']
paises_norte_juntos = reduce(lambda x, y: x + ", " + y, paises_norte)
print_box('Países del norte de Europa'.center(120), 'yellow')
printc(paises_norte_juntos, 'green')
