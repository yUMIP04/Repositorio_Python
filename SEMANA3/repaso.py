import csv

with open("prueba.csv", "w", encoding="utf-8", newline="") as prueba_csv:
    
    campos = ["nombre", "precio", "stock"]
    
    escritor = csv.writer(prueba_csv)
    escritor.writerow(campos)
    
    
with open("prueba.csv", "a", encoding="utf-8", newline="") as prueba_csv:
    escritor2 = csv.writer(prueba_csv)
    escritor2.writerow(["Pan", "12", "200"])
    escritor2.writerow(["Leche", "30", "300"])
   
   
   #🌟Cambiar stock del producto 
productos = []   
with open("prueba.csv", "r", encoding="utf-8", newline="") as prueba_csv:
    lector = csv.DictReader(prueba_csv)
    
    print("Inventario actual:")
    for fila in lector:
        print(f"El producto {fila['nombre']} tiene la cantidad de {fila['stock']} piezas")
        
        productos.append(fila)
        
nombre_producto = input("Ingresa el nombre del producto: ")
cantidad_vendida = int(input("Ingresa la catidad vendida: "))

print(f"El producto a vender es {nombre_producto} y vas a vender la cantidad {cantidad_vendida}")

encontrado = False

for fila in productos:
    if fila["nombre"].lower() == nombre_producto.lower():
        stock_actual = int(fila["stock"])
        
        if cantidad_vendida >  stock_actual:
            print(f"El {nombre_producto} no tiene suficiente cantidad para vender.")
            
        else:
            nuevo_stock = stock_actual - cantidad_vendida
            fila["stock"] = str(nuevo_stock)
            print(f"El {nombre_producto} se ha vendido y resta {fila["stock"]} unidades.") 
            encontrado = True
            break
if not encontrado:
    print("producto no encontrado")
    
with open("prueba.csv", "w", encoding="utf-8", newline="") as prueba_csv:
      campos = ["nombre", "precio", "stock"]
      escritor3 = csv.DictWriter(prueba_csv, fieldnames=campos)
      escritor3.writeheader()
      escritor3.writerows(productos)
      
      print("Archivo actualizado corectamente")