import csv


#🌟Leer
with open("data.csv", "r", newline="", encoding="utf-8") as archivo:
    
    lector = csv.reader(archivo)
    
    for fila in lector:
        
        print(fila)
        

#🌟ESCRIBIR

cabeceras = ["Nombre", "Edad", "Pais"]
with open("repaso.csv", "w", newline="", encoding="utf-8") as repaso:
     escritor = csv.writer(repaso)
     escritor.writerow(cabeceras)#CABECERA
     escritor.writerow(["Ana", "23", "Mexico"])#FILAS


#🌟CSV.READER()

with open("repaso.csv", "r", newline="", encoding="utf-8") as repaso:
    
    lector2=csv.DictReader(repaso)
    
    for fila in lector2:
        print(fila["Nombre"], fila["Edad"])
        
#🌟CSV.DICWRITER(archiv, fieldnames=lista)

with open("repaso2.csv", "w", newline="", encoding="utf-8") as repaso:
    
    campos = ["Nombre", "Edad", "Pais"]
    
    escritor2 = csv.DictWriter(repaso, fieldnames=campos)
    escritor2.writeheader()
    escritor2.writerow({"Nombre": "Ana", "Edad": 23, "Pais": "Mexico"})