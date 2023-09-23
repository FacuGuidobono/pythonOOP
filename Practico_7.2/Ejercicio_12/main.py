'''
+--------------------------------------------------------------------+
|                        Ejercicio 12                                |
|                                                                    |
|   lista que contiene los elementos de l excepto aquellos elementos |
|            para los cuales el predicado p es verdadero.            |
|                                                                    |
+--------------------------------------------------------------------+


'''
from modulos.decorators import *

def remove_if(p: callable , l: list = None) -> list:

  return list(filter(lambda x: not p(x), l))



def main():

  #----------------------------------------------------------------
  print_box("Se eliminaran todos los elementos de la lista que son pares [x % 2 == 0]","red")
  p = lambda x: x % 2 == 0 # elimina todos los elementos de la lista que son pares
  old_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
  printc(f"Lista original: {old_lista}\n", "blue")
  new_lista = remove_if(p, old_lista)
  printc(f"Lista modificada: {new_lista}\n", "green")
#------------------------------------------------------------------
  msg_continuar()
  clear_console()
#------------------------------------------------------------------
  print_box("Se eliminaran todos los elementos de la lista que son multiplos de tres [x % 3 == 0]","yellow")
  p = lambda x: x % 3 == 0 # elimina todos los elementos de la lista que son multiplos de 3
  printc(f"Lista original: {old_lista}\n", "blue")
  new_lista = remove_if(p, old_lista)
  printc(f"Lista modificada: {new_lista}\n", "green")
  msg_continuar()

if __name__ == "__main__":
   clear_console()
   main()
   clear_console()