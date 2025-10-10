#🌟MINIPROYECTO
import csv

with open("Productos_Tienda.csv", "w", encoding="utf-8", newline="") as productos_csv:
    campos = ["nombre", "precio", "stock"]
    escritor = csv.writer(productos_csv)
    escritor.writerow(campos)
    

class Producto:
    
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        

class Tienda:
    
    def __init__(self, lista_productos):
        self.lista_productos = lista_productos
        
    def agregar_producto(self, producto:Producto):
        with open("Productos_Tienda.csv", "a", encoding="utf-8", newline="") as productos_csv:
            escritor = csv.writer(productos_csv)
            escritor.writerow([producto.nombre, producto.precio, producto.stock])
    
    def mostrar_producto(self):
        with open("Productos_Tienda.csv", "r", encoding="utf-8", newline="") as productos_csv:
            lector = csv.reader(productos_csv)
            
            for fila in lector:
                print(fila)
    
    def vender_producto(self):
        
        producto_nombre = input("Ingresa el producto que quieres vender: ")
     
        with open("Productos_Tienda.csv", "r", encoding="utf-8", newline="") as productos_csv:
            lector2 = csv.reader(productos_csv)
            header = next(lector2)
            filas = []
            
            for productos in lector2:
                nombre = productos[0]
                precio = productos[1]
                stock = int(productos[2].strip())
                
                print(f"Producto:{nombre}, Precio_ {precio}, Stock: {stock}")
                
               
                
                if nombre.strip().lower() == producto_nombre.strip().lower():
                    if stock > 0:
                        stock -=1
                        
                        productos[2] = str(stock)
                        print(f"Vendido 1 {nombre}, Nuevo stock {stock}.")
                        
                    else:
                        print(f"No hay stock de {nombre}")
                filas.append(productos)  
                     
        with open("Productos_Tienda.csv", "w", encoding="utf-8", newline="") as productos_csv:
            escritor3 = csv.writer(productos_csv)
            escritor3.writerow(header)
            escritor3.writerows(filas)
            
producto1 = Producto("Manzana", 10.5, 20)
producto2 = Producto("Pan", 5.0, 15)

mi_tienda = Tienda([])

mi_tienda.agregar_producto(producto1)
mi_tienda.agregar_producto(producto2)

mi_tienda.mostrar_producto()
mi_tienda.vender_producto()