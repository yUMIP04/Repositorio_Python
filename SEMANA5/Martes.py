import sqlite3

conexion = sqlite3.connect("productos.db")
cursor = conexion.cursor()

cursor = conexion.execute('''
    CREATE TABLE IF NOT EXISTS productos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        precio REAL,
        stock INTEGER    
    )                     
    ''')

def agregar_producto(nombre, precio, stock):
    cursor = conexion.cursor()
    
    cursor.execute(
        '''
        INSERT INTO productos (nombre, precio, stock) VALUES
        (?,?,?)
        ''', (nombre, precio, stock)
    )
    
    conexion.commit()
    print("☑️Se insertaron correctamente los nuevos productos.")
    
    
def  ver_productos():
    
    cursor = conexion.cursor()
    
    cursor.execute(
        'SELECT * FROM productos'
    )
    
    productos = cursor.fetchall()
    
    for producto in productos:
        print(producto)
        
        
def actualizar_stock(id, nuevo_stock):
    cursor = conexion.cursor()
    
    cursor.execute(
        '''
        UPDATE productos SET stock = ?
        WHERE id = ? 
        ''',(id, nuevo_stock)
    )
    
    conexion.commit()
    print("Se hizo la actualizacion de manera correcta")
    
    
agregar_producto("maruchan", 1.50, 300)
ver_productos()
actualizar_stock(1,200)