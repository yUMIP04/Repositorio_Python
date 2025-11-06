import sqlite3

conexion = sqlite3.connect('inventarios.db')

cursor = conexion.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS productos(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nombre TEXT,
                   precio REAL,
                   stock INTEGER
               )
               ''')

cursor.execute('''
               INSERT INTO productos(nombre, precio, stock) VALUES
               ('Cereal', 74, 300),
                   ('Carne', 200, 400)
               
               ''')

cursor.execute('SELECT * FROM productos')
productos = cursor.fetchall()

for producto in productos:
    print(producto)

conexion.commit()
conexion.close()


