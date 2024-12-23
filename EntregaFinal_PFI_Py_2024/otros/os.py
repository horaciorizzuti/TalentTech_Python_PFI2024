# import os
# print(f"Directorio actual: {os.getcwd()}")

# diccionario_categorias = {
#     1:{categoria_numero:}
# }


# for clave, valor in diccionario_categorias. items():
#     print(clave, valor. get("categoria"))
#     categoria_numero = int (input ("Ingrese el numero de la categoria: "))
#     categoria_nombre = diccionario_categorias [categoria_numero][ "categoria"]

# Diccionario de categorías
diccionario_categorias = {
    1: {"categoria": "Electrónica"},
    2: {"categoria": "Hogar"},
    3: {"categoria": "Deportes"},
    4: {"categoria": "Moda"}
}

# Recorremos el diccionario e imprimimos las categorías
for clave, valor in diccionario_categorias.items():
    print(f"{clave}: {valor.get('categoria')}")

# Pedimos al usuario que elija una categoría
categoria_numero = int(input("Ingrese el número de la categoría: "))

# Validamos si la categoría ingresada existe en el diccionario
if categoria_numero in diccionario_categorias:
    categoria_nombre = diccionario_categorias[categoria_numero]["categoria"]
    print(f"Has seleccionado la categoría: {categoria_nombre}")
else:
    print("El número ingresado no corresponde a una categoría válida.")
