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
        ''',(nuevo_stock, id)
    )
    
    conexion.commit()
    print("Se hizo la actualizacion de manera correcta")
    
def eliminar_producto(nombre):
    cursor = conexion.cursor()
    
    cursor.execute(
        '''DELETE FROM productos WHERE nombre = ?''',(nombre,)
    )
    
    conexion.commit()


while True:
    
    print("--Bienvenido al menu de opciones--")
    print("1. Agregar producto a la base de datos.")
    print("2. Ver la tabla de base de datos.")
    print("3. Actualizar el stock.")
    print("4. Eliminar un producto.")
    print("5. Salir.")
    
    option = input("Elige una de las opciones: ")
    
    match option:
        
        case "1":
            nombre = input("Inserta el nombre: ")
            precio = input("Inserta el precio: ")
            stock = input("Inserta el stock: ")
            agregar_producto(nombre, precio, stock)
            
        case "2":
            ver_productos()
            
        case "3":
            id = int(input("Inserta el id: "))
            stock = int(input("Inserta el stock: "))
            actualizar_stock(id, stock)
            
        case "4":
            nombre= input("Inserta el nombre del producto: ")
            eliminar_producto(nombre)
            
        case "5":
            print("Saliendo del programa...")
            break
        
        case _:
            print("Elige una de las opciones que se te muestran.")