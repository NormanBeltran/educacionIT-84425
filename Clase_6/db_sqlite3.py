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

def insertar():
    personas = (
        (1, "Jose", 500000, "Finanzas", "Jefe", "2010-01-01", 40),
        (2, "Maria", 700000, "IT", "Gerente", "2011-01-01", 35),
        (3, "Ana", 400000, "Compras", "Supervisor", "2010-04-01", 50),
        (4, "Pedro", 300000, "Legales", "Administrativo", "2015-01-01", 20),
        (5, "Juana", 200000, "Ventas", "Cadete", "2010-06-01", 18),
        (6, "Pablo", 800000, "RRHH", "Administrativo", "2017-06-01", 41)        
    )    

    for nid, nombre, salario, depto, posicion, fingreso, edad in personas:
        cursor.execute("""
            INSERT INTO empleados VALUES (?,?,?,?,?,?,?) 
        """, (nid, nombre, salario, depto, posicion, fingreso, edad))
    conn.commit()

def insertar_uno(nid, nombre, salario, depto, posicion, fingreso, edad):
    cursor.execute("""
            INSERT INTO empleados VALUES (?,?,?,?,?,?,?) 
        """, (nid, nombre, salario, depto, posicion, fingreso, edad))
    conn.commit()

def actualizar():
    cursor.execute("""
            UPDATE empleados SET posicion = 'Jefe', salario = 1200000 WHERE id = 6
        """)
    conn.commit()

def consultar():
    cursor.execute("SELECT * FROM empleados")
    filas = cursor.fetchall()
    for f in filas:
        print(f)

def consultar_uno(id):
    cursor.execute("SELECT * FROM empleados WHERE id = " + str(id))
    fila = cursor.fetchone()
    print(fila)

def consultar_like(patron):
    sentencia = "SELECT * FROM empleados WHERE nombre LIKE ?;"
    cursor.execute(sentencia, [f"%{patron}%"] )
    filas = cursor.fetchall()
    for f in filas:
        print(f)    

def borrar_uno(id):
    cursor.execute("DELETE FROM empleados WHERE id = " + str(id))
    conn.commit()

#__________________________________ Main

conn = sqlite3.connect("empleados.db") # Creamos el objeto de conexión a la BD
cursor = conn.cursor() # Es un objeto que nos va a permitir hacer operaciones en la BD

# Crear una tabla
#crearTabla()

# Insertar registros en la BD
# insertar()

# Insertar un solo registro
# insertar_uno(7, "Mariana", 900000, "IT", "Directora", "2005-01-01", 50)

# Actualizar un dato de un registro
# actualizar()

# Consultar
# consultar()

# Consulta un registro por id
# consultar_uno(2)

# Consulta registros cuyo nombre tenga un patron
# consultar_like("na")

borrar_uno(5)
consultar()

conn.close() # Cerrando la conexión - Ojo es importante