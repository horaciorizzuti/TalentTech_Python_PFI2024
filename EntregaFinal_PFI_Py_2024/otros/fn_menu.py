# Se importan los modulos y funciones 
from fn_db import * # noqa: F403
from fn_check import * # noqa: F403
from tabulate import tabulate # modulo para la tabulación de los datos obtenidos de la DB

msg_succ = "Proceso efectuado con exito"
msg_nf = "Productos no encontrados"

# Se define la funcion de inicio y las funciones que retornan valores segun elección
# def mn_start():
#     print("\n")
#     print("*" * 50)
#     print("    Menú de inicio")
#     print("*" * 50)
#     print("""
#     1. Agregar producto
#     2. Visualizar producto
#     3. Actualizar la cantidad de un productos
#     4. Eliminar producto
#     5. Buscar producto
#     6. Reporte bajo Stock
#     7. Salir del sistema de inventario
#         """)
#     menu = input("Ingrese la opción deseada: ")
#     return menu

def mn_start():
    menu_items = [
        [f'\033[1mMENU DE INICIO\033[0m'],
        [f'\033[1mOpcion\033[0m',f'\033[1mProceso\033[0m'], 
        ["1", "Agregar producto"],
        ["2", "Visualizar producto"],
        ["3", "Actualizar la cantidad de un producto"],
        ["4", "Eliminar producto"],
        ["5", "Buscar producto"],
        ["6", "Reporte bajo Stock"],
        ["7", "Salir del sistema de inventario"],
    ]

    print("\n" + tabulate(menu_items, headers="firstrow", tablefmt="fancy_grid", stralign="left"))
    menu = input("Ingrese la opción deseada: ")
    return menu


def mn_add():
    print("\n Ingrese el producto:")
    nombre = check_name()
    descripcion = check_descr()
    categoria = check_cat()
    cantidad = check_qty()
    precio = check_pr()

    producto = {
        "nombre": nombre,
        "descripcion": descripcion,
        "categoria": categoria,
        "cantidad": cantidad,
        "precio": precio,
    }
    db_insert(producto)
    print("\n" + msg_succ)


# def mn_list():
#     lista = db_read()
#     if lista:
#         for producto in lista:
#             print(producto)
#     else:
#         print(f'\n {msg_nf} en la base de datos')

# visualización de db tabulada
def mn_list():
    #lista = db_read()
    lista, headers = db_read()
    if lista:
        # headers = ["ID", "Nombre", "Descripción", "Categoría", "Cantidad", "Precio"]
        print(tabulate(lista, headers=headers, tablefmt="fancy_grid")) # grid
    else:
        print(f'\n {msg_nf} en la base de datos')


def mn_alter():
    mn_list()
    id = int(input("\n Ingrese el id del producto que desea modificar la cantidad: "))
    id_producto = db_read_id(id)
    if not id_producto:
        print(f'{msg_nf} con el id {id}')
    else:
        print(f"Cantidad actual {id_producto[4]} ")
        # nueva_cantidad = check_qty("Nueva cantidad")
        nueva_cantidad = check_qty() # modificado por new_qty
        db_update(id, nueva_cantidad)
        print("\n" + msg_succ)


def mn_del():
    mn_list()
    id = int(input("\n Ingrese el id del producto a eliminar: "))
    id_producto = db_read_id(id)
    if not id_producto:
        print(f"{msg_nf} con ID: {id}")
    else:
        print("\n Se eliminará el siguiente registro:")
        print(id_producto)
        borrar = input(
            "\n presione 'Y' para confirmar la eliminación del producto o enter para abortar: ").lower()
        if borrar == "y":
            db_delete(id)
            print("\n" + msg_succ)
        else:
            print("Operación cancelada.")


def mn_search():
    id = int(input("\n Ingrese el id del producto que desea consultar: "))
    id_producto, headers = db_read_id(id)
    #id_producto = db_read_id(id)
    if not id_producto:
        print(f"{msg_nf} con ID: {id}")
    else:
        #print(id_producto)
        print(tabulate(id_producto, headers=headers, tablefmt="fancy_grid")) 


def mn_stk_min():
    # stock_min = int(input("\n Ingrese el stock mínimo por categoria:"))
    # lista = db_read_st_min(stock_min)
    lista = db_read_st_min()
    if not lista:
        print("No se ha encontrado ningún producto con stock menor a {stock_min}")
    else:
        for producto in lista:
            print(producto)
