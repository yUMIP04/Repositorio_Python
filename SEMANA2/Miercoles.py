#🌟ARCHIVOS

txt = open("texto3.txt", "a")



txt.write("Ho")
txt = open("texto3.txt", "r")
print(txt.read())

#🌟CSV

import pandas as pd

#df = pd.read_csv('data.csv')
#print(df.to_string())
#print(pd.options.display.max_rows)

#pd.options.display.max_rows = 999

#df = pd.read_csv('data.csv')
#print(df)

import csv

with open("data.csv", newline="", encoding="utf-8") as archivo:
 
    #lector = csv.reader(archivo)
    lector = csv.DictReader(archivo)
    
    for fila in lector:
        
        print(fila["Duration"], fila["Pulse"], fila["Maxpulse"], fila["Calories"])
  
#🌟CREAR UN CSV      
contactos = [
    ["nombre", "telefono", "email"],
    ["Juan", "123", "juan@gmail.com"],
    ["Ana", "456", "ana@gmail.com"]
]

with open("contactos.csv", "w", newline="", encoding="utf-8" ) as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(contactos)
        
contactos2 = [
    {"nombre": "Juan", "telefono": "123", "email":"juan@gmail.com"},
    {"nombre": "Ana", "telefono": "456", "email": "ana@gmail.com"}
]

with open("contactos2.csv", "w", newline="", encoding="utf-8") as archivo2:
    campos = ["nombre", "telefono", "email"]
    escritor2 = csv.DictWriter(archivo2, fieldnames=campos)
    
    escritor2.writeheader()
    escritor2.writerows(contactos2)
    
    
#🌟LEER TODO EN UNA LISTA DE DICCIONARIOS
contactos3 = [
    {"nombre": "Juan", "telefono": "123", "email":"juan@gmail.com"},
    {"nombre": "Ana", "telefono": "456", "email": "ana@gmail.com"}
]
with open("contactos.csv", newline="", encoding="utf-8") as archivo3:
    lector = csv.DictReader(archivo3)
    contactos3 = list(lector)
    
    
#🌟EJERCICIOS



with open("datos.txt", "r") as ejercicio_txt:
    print(ejercicio_txt.read())
    
    
#🌟MINIRETO
suma = 0
promedio = 0
calificaciones_lista = []
for calificacion in range(5):
    
    calificacion = input("Ingresa 5 calificaciones para saber tu promedio: ")
    numeros = int(calificacion)
    calificaciones_lista.append(numeros)
    
    suma = sum(calificaciones_lista)
    promedio = suma / len(calificaciones_lista)
    
    with open("calificaciones.txt", "w") as calificaciones_archivo:
        calificaciones_archivo.write(f"Estas son las calificaciones: {calificaciones_lista}\n")
        calificaciones_archivo.write(f"Este es el promedio: {promedio}")
        
with open("calificaciones.txt", "r") as calificaciones_archivo:
    print(calificaciones_archivo.read())