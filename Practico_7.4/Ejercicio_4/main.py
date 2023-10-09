

def ordenar_por_edad(lista):
    return sorted(lista, key=lambda x: x[1])






def ordenar_por_nombre(lista):
    return sorted(lista, key=lambda x: x[0])

# Ejemplo de uso
personas = [('Alice', 25), ('Bob', 30), ('Eve', 22), ('David', 28)]
personas_ordenadas_por_nombre = ordenar_por_nombre(personas)
print(personas_ordenadas_por_nombre)
personas_ordenadas_por_edad = ordenar_por_edad(personas)
print(personas_ordenadas_por_edad)