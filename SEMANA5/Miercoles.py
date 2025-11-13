from flask import Flask, g
import sqlite3

app = Flask(__name__)

def get_db():
    
    if 'db' not in g:
        g.db = sqlite3.connect('inventario.db')
    return g.db

def create_table():
    
    db = get_db()
    cursor = db.cursor()
    
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS productos(
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            precio REAL,
            stock INTEGER
        )
        '''
    )
    
    db.commit()
    
def agregar_productos():
    db = get_db()
    cursor = db.cursor()
    
    cursor.execute(
        '''
        INSERT INTO productos(nombre, precio, stock)VALUES
        ('Cereal', 12.50, 500)
        '''
    )
    
    db.commit()
    print("Se adjuntaron nuevos productos")
    


@app.route('/')

def pagina_inicio():
    
    print("Esta es la pagina de inicio")
    return 'Bienvenido a la pagina de inicio'
    
    
@app.route('/productos')

def pagina_productos():
    
    db = get_db()
    cursor = db.cursor()
    
    
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    resultado = '<h2>Lista de productos</h2>'
    
    if not productos:
        resultado += '<h2>No hay productos en la base de datos</h2>'
        
    else:
      for producto in productos:
          resultado += f'ID : {producto[0]}, NOMBRE: {producto[1]}, PRECIO: {producto[2]}, STOCK: {producto[3]}<br>'
    return resultado


        
    
if __name__ == '__main__':
    with app.app_context():
        create_table()
        agregar_productos()
    app.run(debug=True)
    