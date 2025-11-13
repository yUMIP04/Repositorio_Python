from flask import Flask, g, request, render_template
import sqlite3

app = Flask(__name__)

#🌟BD
def creacion_bd():
    if 'db' not in g:
        g.db = sqlite3.connect('Tienda.db')
    return g.db
    
def creacion_table():
    conexion = creacion_bd()
    cursor = conexion.cursor()
    
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS productos_tienda(
            id INTEGER PRIMARY KEY,
            nombre VARCHAR,
            precio REAL,
            stock INTEGER
        )
        '''
    ) 
    conexion.commit()
    
    


#🌟BIENVENIDO A LA PAGINA DE BIENVENIDA
@app.route('/')

def pagina_bienvenida():
    return '🌟🥸Bienvenido a la pagina'


#🌟PAGINA DEL FORMULARIO

@app.route('/formulario', methods=['GET', 'POST'])

def pagina_formulario():
    nombre = ''
    precio = ''
    stock = ''
    
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        stock = request.form['stock']
        
        conexion = creacion_bd()
        cursor = conexion.cursor()
        
        cursor.execute(
            'INSERT INTO productos_tienda (nombre,precio,stock)VALUES(?,?,?)', (nombre,precio,stock)
        )       
        conexion.commit()
       
        
        return '☑️El producto a sido agregado correctamente a la base de datos.' 
    
    return render_template('formulario.html')


@app.route('/productos', methods = ['GET'])

def mostrar_productos():
    
    conexion = creacion_bd()
    cursor = conexion.cursor()
    
    cursor.execute('SELECT * FROM productos_tienda')
    productos = cursor.fetchall()
    conexion.close()
    
    return render_template('productos.html', productos=productos)





#

if __name__ == '__main__':
    with app.app_context():
     creacion_table()
    app.run(debug=True)
    
conexion = sqlite3.connect('Tienda.db')
cursor = conexion.cursor()
cursor.execute("SELECT * FROM productos_tienda")
print(cursor.fetchall())
conexion.close()