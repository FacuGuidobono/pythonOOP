'''
+====================================================================================+
|                                                                                    |
|  ordenar una lista de duplas por el primer ítem (nombre) o el segundo ítem (edad)  |          
|                                                                                    |
+====================================================================================+    '''
from decorators import *


def sumarSi(f, l):
    # Inicializamos la suma en 0
    suma = 0
    # Iteramos sobre la lista
    for elemento in l:
        # Comprobamos si el elemento cumple la condición
        if f(elemento):
            suma += elemento
    return suma

def main():
    # Asignar la función a una variable
    mi_funcion = sumarSi

    # Definir una función f que verifica si un número es par
    def es_par(numero):
        return numero % 2 == 0

    # Crear una lista de números

    numeros = [  validar_un_input(f"Ingrese un número : ", int) for _ in range(10)]

    # Invoque la función a través de la variable
    resultado = mi_funcion(es_par, numeros)
    print("La suma de números pares es:", resultado)


if __name__ == "__main__":
    main()  