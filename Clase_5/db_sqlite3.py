import sqlite3


def crearTabla():
    cursor.execute("""
        CREATE TABLE empleados (
                   id           integer PRIMARY KEY,
                   nombre       text,
                   salario      real,
                   departamento text,
                   posicion     text,
                   ingreso      text,
                   edad         numeric
        )
    """)
    conn.commit()

#__________________________________ Main

conn = sqlite3.connect("empleados.db") # Creamos el objeto de conexión a la BD
cursor = conn.cursor() # Es un objeto que nos va a permitir hacer operaciones en la BD

# Crear una tabla
crearTabla()

conn.close() # Cerrando la conexión - Ojo es importante