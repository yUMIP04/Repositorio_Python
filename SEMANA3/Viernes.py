#🌟MINI PROYECTO
import csv

with open("inventario.csv", "w", encoding="utf-8", newline="") as archivo_inventario:
    
    campos = ["nombre", "precio", "stock"]
    escritor = csv.writer(archivo_inventario)
    escritor.writerow(campos)


class Producto:
    
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        
class Inventario:
    
    def __init__(self):
        self.list_productos = []
        
    def agregar(self, producto:Producto):
        
        try:
         with open("inventario.csv", "a", encoding="utf-8", newline="") as archivo_inventario:
             escritor2 = csv.writer(archivo_inventario)
             escritor2.writerow([producto.nombre, producto.precio, producto.stock])
             self.list_productos.append(producto)
            
        except Exception as e:
            print(f"❌Hubo un error al intentar agregar informacion {e}.")
            
    def vender(self):
        try:
            productos = []

            
            with open("inventario.csv", "r", encoding="utf-8", newline="") as archivo_inventario:
                lector = csv.DictReader(archivo_inventario)

                print("📦 Inventario actual:")
                for fila in lector:
                    print(f" - {fila['nombre']} tiene {fila['stock']} unidades.")
                    productos.append(fila)

            
            nombre_producto = input(" Escribe el nombre del producto que quieres vender: ").lower()
            cantidad_vendida = int(input(" Escribe la cantidad que quieres vender: "))

          
            encontrado = False
            for fila in productos:
                if fila["nombre"].lower() == nombre_producto:
                    stock_actual = int(fila["stock"])
                    if cantidad_vendida > stock_actual:
                        print("❌ No hay suficientes unidades para vender.")
                    else:
                        nuevo_stock = stock_actual - cantidad_vendida
                        fila["stock"] = str(nuevo_stock)
                        print(f"Vendiste {cantidad_vendida} unidades de {fila['nombre']}. Quedan {nuevo_stock}.")
                    encontrado = True
                    break

            if not encontrado:
                print("❌ El artículo no existe en el inventario.")

           
            with open("inventario.csv", "w", encoding="utf-8", newline="") as archivo_inventario:
                campos = ["nombre", "precio", "stock"]
                escritor2 = csv.DictWriter(archivo_inventario, fieldnames=campos)
                escritor2.writeheader()
                escritor2.writerows(productos)

            print(" Archivo actualizado correctamente.")

        except Exception as e:
            print(f"❌ Hubo un error en la operación: {e}")    
    
    def mostrar(self):
        try:
            with open("inventario.csv", "r", encoding="utf-8", newline="") as archivo_inventario:
                lector3= csv.reader(archivo_inventario)
                
                for informacion in lector3:
                    print(informacion)
                    
        except Exception as e:
                print("Error al mostrar informacion.")
                
                
producto1 = Producto("Pan", "7", "200")
inventario1 = Inventario()
inventario1.agregar(producto1)
inventario1.vender()