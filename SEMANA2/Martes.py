#🌟DICCIONARIOS ANIDADOS


niño1 = {
        "name":"Victoria",
        "age" : 21
         }
    
    
niño2 = {
        "name": "Luis",
        "age": 21
    }


diccionario2 = {
    "niño1" : niño1,
    "niño2" : niño2
}
print(diccionario2)
print(diccionario2["niño1"]["name"])

for obj in diccionario2.items():
    print(obj)
    
#🌟METODOS DE UN DICCIONARIO

print(diccionario2.get("niño1").get("name"))
print(diccionario2["niño1"].keys())
print(diccionario2.values())
print(diccionario2["niño1"].items())
diccionario2["niño1"]["cumpleaños"] = "12 Abril"
print(diccionario2["niño1"])
print(diccionario2["niño2"].update({"cumpleaños": "30 Abril" }))
print(diccionario2["niño2"])
print(diccionario2["niño2"].pop("cumpleaños"))
print(diccionario2["niño2"])
print(diccionario2["niño1"].popitem())
print(diccionario2["niño1"])
print(diccionario2["niño1"].fromkeys("name", 0))
print(diccionario2["niño1"].setdefault("name"))

alumnos = {
    "alumno1": "Victoria",
    "alumno2" : "Enzo",
    "alumno3": "Bryan"
}

calificaciones = {
    "alumno1_cal": 10,
    "alumno2_cal": 9,
    "alumno3_cal":8
}

materias = {
    "materia1": "Matematicas",
    "materia2": "Español",
    "materia3": "Historia"
}

for obj2 in alumnos.items(), calificaciones.items(), materias.items():
    print(obj2)
    
Familia_Son = {
    
    "Goku" : {
        "name": "Goku",
        "edad": 40
    },
    
    "Milk": {
        "name": "Milk",
        "edad": 40 
    }
}

print(Familia_Son["Milk"].update({ "edad": 41 }))
print(Familia_Son)

contactos = {
    "Juan": {
        "telefono": "123",
        "email": "juan@gmail.com"
    },
    
    "Ana": {
        "telefono": "456",
        "email": "ana@gmail.com"
    }
}



while True:
    print("-----Bienvenido al diccionario-----")
    print("1.Agregar nuevo contacto.")
    print("2.Buscar contacto.")
    print("3.Mostrar informacion del contacto.")
    print("4.Salir.")
    option = input("Ingresa una opcion o sal del programa: ")
    
    if option == "1":
         print("Bienvenido al area de Agregar usuario")
         option_agregar = input("Ingrese el nombre del contacto: ")
         option_telefono = input("Ingresa el numero de telefono: ")
         option_direccion = input("Ingresa la direccion de correo:")
         print("🌟Contacto guardado de manera exitosa")
     
         contacto_nuevo = {
          "telefono": option_telefono,
          "email" : option_direccion
          }
    
         contactos[option_agregar] = contacto_nuevo
    
    elif option == "2":
        
        option_busqueda = input("Ingresa al contacto que buscas: ")
        
        for busqueda in contactos:
            
            if option_busqueda in busqueda:
                print(f"Este es el usuario que buscas: {option_busqueda}")  
                
    elif option == "3":
        option_info = input("Ingresa el nombre del contacto para obtener su información: ").strip().capitalize()
        
        contacto = contactos.get(option_info)
        
        if contacto:
            print(f"Nombre: {option_info}")
            print(f"Telefono: {contacto['telefono']}")
            print(f"Email: {contacto['email']}")
            
        else:
            print("No existe ese contacto")
            
    elif option == "4":
        print("Saliendo del programa...")
        break