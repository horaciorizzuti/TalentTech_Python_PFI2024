# Se importan los modulos y funciones 
from fn_menu import *  # noqa: F403
from fn_db import db_create


# Se declara la funcion "main" que contiene la logica principal del programa y crea la tabla en bd
def main():

    db_create()

    while True:
        menu = mn_start()
        print("\nOpcion elegida: ", menu, "\n")
        exit = "Salida exitosa del sistema"

        if menu == "1":
            mn_add()
        elif menu == "2":
            mn_list()
        elif menu == "3":
            mn_alter()
        elif menu == "4":
            mn_del()
        elif menu == "5":
            mn_search()
        elif menu == "6":
            mn_stk_min()
        elif menu == "7":
            print("\n"+ exit)
            break
        else:
            print("\n Elija una opción del listado.")

        salir = input("\n presione enter para continuar con el registro de productos o 'X' para salir: " ).lower()
        if salir == "x":
            print("\n"+ exit)
            break
   

# llamada a la función main()
if __name__ == "__main__":
    main()