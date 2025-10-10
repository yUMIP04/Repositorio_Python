import csv 

gasto_max = 0
gasto_min = 0

cabeceras = ["Concepto", "Monton","Fecha"]
with open("Registros.csv", "w", newline="", encoding="utf-8") as documento:
    escritor = csv.writer(documento)
    escritor.writerow(cabeceras)
    
while True:
 print("---Menu del gestor---")
 print("1. Nuevo registro.")
 print("2. Mostrar los gastos.")
 print("3. Gasto alto y gasto bajo.")
 print("4. Salir del gestor.")
 option = input("Ingresa el numero de opcion que prefieras: ")
 
 match option:
     case "1":
        try:
          print("---Bienvenido al area de Registro---") 
         
          concepto = input("Introduce el nombre del producto: ")
          monton = input("Introduce el monton del producto: ")
          fecha = input("Introduce la fecha de la llegada del monton: ")
         
          with open("Registros.csv", "a", newline="", encoding="utf-8") as documento:
             escritor2 = csv.writer(documento)
             escritor2.writerow([concepto, monton,fecha])
             
             print("☑️Se registro correctamente el nuevo producto")
             
        except Exception as e:
            print("❌Error al Registrar nuevo producto")     
     case "2":
        try:
            with open("Registros.csv", "r", newline="", encoding="utf-8") as documento:
                lector3 = csv.DictReader(documento)
              
                for fila in lector3:
                    print(fila["Monton"])
        except Exception as e:
             print("Error al leer el archivo")
     case "3":
        try:
            with open("Registros.csv", "r", newline="", encoding="utf-8") as documento:
                
                lector4 = csv.DictReader(documento)
                
                montos = []
                for fila in lector4:
                    valor = fila["Monton"].strip()
                    
                    if valor.isdigit():
                       
                        
                        montos.append(int(valor)) 
                    
                gasto_max = max(montos)
                gasto_min = min(montos)
                    
                print(f"El gasto maximo es: {gasto_max}")
                print(f"Gasto minimo es: {gasto_min}")
                      
        except Exception as e:
            print("❌Error al ver informacion.")
          
     case "4":
         print("Saliendo del programa...")
         break