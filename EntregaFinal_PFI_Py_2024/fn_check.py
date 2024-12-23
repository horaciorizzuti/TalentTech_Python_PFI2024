# Verificación y validación de datos ingresados en el menú

msg_null = "El campo no puede estar vacío. Por favor, ingrese un valor válido."
msg_invalid = "El valor ingresado no es válido. Inténtelo nuevamente con el formato correcto."

def check_input(nombre_variable, tipo=str, min_valor=None):

    while True:
        try:
            valor = input(f"{nombre_variable}: ").strip()
            if not valor:  
                print(msg_null)
                continue

            valor = tipo(valor)
            
            if min_valor is not None and valor <= min_valor:
                print(f"El valor debe ser mayor a {min_valor}.")
                continue
            
            return valor 
        except ValueError:
            print(msg_invalid)


# Funciones específicas para verificacion de los datos ingresados, reutilizando check_input
def check_name():
    return check_input("Nombre", tipo=str)


def check_descr():
    return input("Descripción: ").strip()


def check_cat():
    return check_input("Categoría", tipo=str)


def check_qty():
    return check_input("Cantidad", tipo=int, min_valor=0)


def check_pr():
    return check_input("Precio", tipo=float, min_valor=0)

def check_stk_min():
    return check_input("Stock minimo", tipo=int, min_valor=0)
