'''
+--------------------------------------------------------------------+
|                                                                    |
|                       Ejercicio 12                                 |
| - lista que contiene los elementos de l excepto aquellos elementos |
|    para los cuales el predicado p es verdadero.                    |
|                                                                    |
+--------------------------------------------------------------------+


'''


def remove_if(p, l):

  return list(filter(lambda x: not p(x), l))