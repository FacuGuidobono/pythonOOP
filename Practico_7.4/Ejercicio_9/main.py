'''
+====================================================================================+
|                                                                                    |
|  Lista de números donde cada número es la suma de los elementos de cada triupla.   |          
|                                                                                    |
+====================================================================================+    '''
from decorators import *

def sumarTriuplas(triuplas):
  sumas = []
  for triupla in triuplas:
    suma = triupla[0] + triupla[1] + triupla[2]
    sumas.append(suma)

  return sumas

def main():
    
    print_box('Suma N° de Triuplas'.center(120),'red')
    triuplas = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    printc(f'Lista de Triuplas: {str(triuplas).center(124)}','yellow')
    printc('-'*124,'magenta',style='bold')
    printc(f'Resultado de las Sumas: {str(sumarTriuplas(triuplas)).center(124)}')
    printc('-'*124,'magenta',style='bold')


if __name__ == "__main__":
    main()


