#🌟USO DEL PRINT()
total = 200
print("Iniciando programa...")
print("Valor total:", total)

#🌟USO DE TRY Y EXCEPT

""" 
try:
    numero = int(input("Ingrese un numero: "))
except ValueError:
    print("Ingrese un numero no una letra.")
    """

"""

#🌟PROGRAMA CON ERRORES INTENCIONALES

"""
#🌟TypeError
"""
try:
    num1 = 200
    num2 = "3"
    print(num1 + num2)
    
except TypeError:
    print("Uno de los elementos no es un entero.")


"""
#🌟ValueError
"""
try:
   numero = int(input("Ingresa una palabra: "))
   print(numero + 12)
except ValueError:
    print("Dato incorrecto.")
    

"""
#🌟KeyError    
"""

diccionario = {
    "name": "Victoria",
    "age": 21
}

try:
    print(diccionario["cumpleaños"])
    
except KeyError:
    print("No se encuentra esa clave en el diccionario.")
    
 """   
#🌟CREA UN MENU CON OPCIONES Y VALIDAR QUE EL USUARIO NO META LETRAS DONDE VA NUMERO:

    
while True:
    print("---Bienvenido al menu---")
    print("1. suma.")
    print("2. resta.")
    print("3. Multiplicacion.")
    print("4. Division.")
    print("5. Salir.")
        
    option = input("Elige una de las opciones: ")
    try:
        match option:
        
            case "1":
            
             print("---Bienvenido al area de suma---")
             suma = 0
            
             for i in range(2):
                
                numero = int(input("Ingresa un numero: "))
                
                suma += numero
                
             print(f"El resultado de la suma es: {suma}")
            
            case "2":
             print("--Bienvenido al area de resta--")
             
             resta = 0
             
             for i in range(2):
                    
                numero = int(input("Ingresa un numero: "))
                
                resta -= numero
                
             print(f"El resultado de la suma es: {resta}")
            
        
            case "3":
              print("--Bienvenido al area de multiplicacion--")
              
              multiplicacion = 1
              for i in range(2):
                  numero = int(input("Ingresa un numero: "))
                  
                  multiplicacion *= numero
                  
              print(f"El resultado de la multiplicacion es: {multiplicacion}")      
            case "4":
             print("--Bienvenido al area de division--")
             
             division = float(input("Ingresa un numero: "))
             division2 = float(input("Ingresa un numero: "))
             
             resultado = division / division2
             
             print(f"El resultado de la division es: {resultado}")
            case "5":
             print("Saaliendo del programa...")
             break
            
            
            case _:
              print("Ingresa una opcion valida.")
              continue
            
    except ValueError:
     print("Ingresa un numero.")