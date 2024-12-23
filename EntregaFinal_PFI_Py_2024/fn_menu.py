# Se importan los modulos y funciones 
from fn_db import * # noqa: F403
from fn_check import * # noqa: F403
from tabulate import tabulate # modulo para la tabulación de los datos obtenidos de la DB

msg_succ = "Proceso efectuado con exito"
msg_nf = "Productos no encontrados"

# Se define la funcion de inicio y las funciones que retornan valores segun elección
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
    stock_minimo = check_stk_min()

    producto = {
        "nombre": nombre,
        "descripcion": descripcion,
        "categoria": categoria,
        "cantidad": cantidad,
        "precio": precio,
        "stock_minimo" : stock_minimo
    }
    db_insert(producto)
    print("\n" + msg_succ)


# visualización db tabulada
def mn_list():
    lista, headers = db_read()
    if lista:
        print(tabulate(lista, headers=headers, tablefmt="fancy_grid")) # plain sin borde
    else:
        print(f'\n {msg_nf} en la base de datos')


def mn_alter():
    mn_list()
    id = int(input("\n Ingrese el id del producto que desea modificar la cantidad: "))
    id_producto, headers = db_read_id(id)
    if not id_producto:
        print(f'{msg_nf} con el id {id}')
    else:
        print(tabulate(id_producto[0:4], headers=headers, tablefmt="fancy_grid")) 
        new_qty = check_qty()
        db_update(id, new_qty)
        print("\n" + msg_succ)


def mn_del():
    mn_list()
    id = int(input("\n Ingrese el id del producto a eliminar: "))
    id_producto, headers = db_read_id(id)
    if not id_producto:
        print(f"{msg_nf} con ID: {id}")
    else:
        print("\n Se eliminará el siguiente registro:")
        # print(id_producto)
        print(tabulate(id_producto, headers=headers, tablefmt="fancy_grid")) 
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
    if not id_producto:
        print(f"{msg_nf} con ID: {id}")
    else:
        #print(id_producto)
        print(tabulate(id_producto, headers=headers, tablefmt="fancy_grid")) 


def mn_stk_min():
    lista, headers = db_read_st_min()
    if not lista:
        print(f'{msg_nf}')
    else:
        print(tabulate(lista, headers=headers, tablefmt="fancy_grid"))
