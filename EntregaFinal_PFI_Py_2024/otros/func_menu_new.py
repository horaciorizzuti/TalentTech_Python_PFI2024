# Se importan los módulos y funciones
from fn_db import *  # noqa: F403
from fn_check import *  # noqa: F403

mensaje, mensaje_e = "Proceso efectuado con exito", "Producto no encontrado con id:"

# Se define la funcion de inicio y las funciones que retornan valores segun elección
def mn_start():
    print("*" * 35 + "\n Menú de inicio\n" + "*" * 35)
    print("""
          1. Agregar producto
          2. Visualizar producto
          3. Actualizar la cantidad de un producto
          4. Eliminar producto
          5. Buscar producto
          6. Reporte bajo Stock
          7. Salir del sistema de inventario
        """)
    return input("Ingrese la opción deseada: ")

def mn_add():
    db_insert({
        "nombre": check_name(), "descripcion": check_descr(),
        "categoria": check_cat(), "cantidad": check_qty(), "precio": check_pr()
    })
    print("\n" + mensaje)

def mn_list():
    lista = db_read()
    print("\n".join(map(str, lista)) if lista else "No hay productos en la base de datos")

def mn_alter():
    id = int(input("\nIngrese el id del producto a actualizar: "))
    if id_producto := db_read_id(id):
        db_update(id, check_qty(f"Nueva cantidad (actual: {id_producto[4]}): "))
        print("\n" + mensaje)
    else:
        print(f"ERROR: no se ha encontrado ningún producto con el id {id}")

def mn_del():
    id = int(input("\nIngrese el id del producto a eliminar: "))
    if id_producto := db_read_id(id):
        print("\nATENCION: se eliminará el siguiente registro:\n", id_producto)
        if input("\nPresione 'x' para confirmar o Enter para abortar: ").lower() == "x":
            db_delete(id)
            print("\n" + mensaje)
        else:
            print("Operación cancelada.")
    else:
        print(f"{mensaje_e} {id}")

def mn_search():
    id = int(input("\nIngrese el id del producto que desea consultar: "))
    print(db_read_id(id) or f"{mensaje_e} {id}")

def mn_stk_min():
    stock_min = int(input("\nIngrese el stock mínimo por categoría: "))
    lista = db_read_st_min(stock_min)
    print("\n".join(map(str, lista)) if lista else f"No se ha encontrado ningún producto con stock menor a {stock_min}")
