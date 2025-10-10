lista_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in lista_number:
    
    if numero % 2 == 0:
        print(numero)
        
"""
lista2 = []

usuario = ""
while usuario != "salir":
    usuario = input("Ingresa numeros: ")
    
    if usuario == "salir":
        break
    lista2.append(usuario)
    sin_repetir =list(set(lista2))
print(lista2)

print(f"Lista sin repetir: {sin_repetir}")


 """
 
usuario = ""
promedio = 0
lista_calificaciones = []
suma = 0
while usuario != "fin":
    usuario = input("Ingresa calificaciones: ")
    
    if usuario == "fin":
        break
    lista_calificaciones.append(usuario)
    
    
    for numeros in lista_calificaciones:
        if numeros.isdigit():
         numbers = int(numeros)
        
        suma += numbers
        
        promedio = suma / len(lista_calificaciones)
        
print(f"Este es el promedio: {promedio}")