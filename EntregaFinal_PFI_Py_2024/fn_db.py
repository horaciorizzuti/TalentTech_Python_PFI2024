# se importa el modulo de sqlite para inicializar, crear y modelar la db
import sqlite3 as sq3


# se declara la funcion "con_db" y "create_table" para conectar con db,crear la tabla y realizar CRUD
def db_con():
    try:
        global con, cur
        con = sq3.connect("inventory.db")
        cur = con.cursor()
        return con, cur
    except sq3.Error as e:
        print(f"Error de conexión a la base de datos: {e}")


def db_create():
    try:
        con, cur = db_con()
        cur.execute(
            """CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                categoria TEXT NOT NULL,
                cantidad INTEGER NOT NULL,
                precio REAL NOT NULL,
                stock_minimo INTEGER
            )"""
        )
        con.commit()

    except sq3.Error as e:
        print(f"No se creó la tabla. Error: {e}")
    finally:
        con.close()

def db_insert(producto):
    db_con()
    query = "INSERT INTO productos (nombre, descripcion, categoria, cantidad, precio, stock_minimo) VALUES (?,?,?,?,?,?)"
    insert_val = (
        producto["nombre"],
        producto["descripcion"],
        producto["categoria"],
        producto["cantidad"],
        producto["precio"],
        producto["stock_minimo"]
    )

    cur.execute(query, insert_val)
    con.commit()
    con.close()


def db_read():
    db_con()
    query = "SELECT * FROM productos"
    cur.execute(query)
    lista = cur.fetchall()  # cur.fetchone() retorna tupla
    headers = [desc[0].capitalize() for desc in cur.description] # agregado para tabulacion
    con.close()
    return lista, headers 


def db_read_id(id):
    db_con()
    query = "SELECT * FROM productos WHERE id = ?"
    insert_val = (id,)
    cur.execute(query, insert_val)
    # product = cur.fetchone()
    product = cur.fetchall()
    headers = [desc[0].capitalize() for desc in cur.description] # agregado para tabulacion
    con.close()
    return product, headers


def db_update(id, new_qty):
    db_con()
    query = "UPDATE productos SET cantidad = ? WHERE id = ?"
    insert_val = (new_qty, id)
    cur.execute(query, insert_val)
    con.commit()
    con.close()


def db_delete(id):
    db_con()
    query = "DELETE FROM productos WHERE id = ?"
    insert_val = (id,)
    cur.execute(query, insert_val)
    con.commit()
    con.close()


def db_read_st_min():
    db_con()
    query = "SELECT * FROM productos WHERE cantidad < ?"
    insert_val = "stock_minimo"
    cur.execute(query, insert_val)
    prod = cur.fetchall()
    con.close()
    return prod

