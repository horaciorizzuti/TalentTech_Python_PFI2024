# Verificación y validación de datos ingresados en el menu

msg_null = "El campo no puede estar vacío. Por favor, ingrese un valor válido."
msg_invalid = "El valor ingresado no es válido. Inténtelo nuevamente con el formato correcto."


def check_name():
    while True:
        nombre = input("Nombre: ").strip()
        if nombre:
            break
        else:
            print("\n" + msg_null)
    return nombre


def check_descr():
    descripcion = input("Descripción: ").strip()
    return descripcion


def check_cat():
    while True:
        categoria = input("Categoría: ").strip()
        if not categoria:
            print("\n" + msg_null)
        else:
            return categoria


def check_qty(mensaje="Cantidad: "):
    while True:
        try:
            cantidad = int(input(f"{mensaje} ").strip())
            if not cantidad:
                print("\n" + msg_null)
            elif cantidad <= 0:
                print("\n" + msg_invalid)
            else:
                return cantidad

        except ValueError:
            print("\n" + msg_invalid)


def check_pr():
    while True:
        try:
            precio = float(input("Precio: ").strip())
            if not precio:
                print("\n" + msg_null)
            else:
                return precio

        except ValueError:
            print("\n" + msg_invalid)
