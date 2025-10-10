def par_impar(numero):
    
    if numero % 2 == 0:
        
        print(f"Este numero es par: {numero}")
        return numero
        
    else:
        print(f"Este numero es impar: {numero}")
        


for number in range(1, 20):
    
    if number % 3 == 0:
     print(number)
     

def suma_lista(lista_numeros:list):
    
    suma = 0
    for numero in lista_numeros:
        suma += numero
        
    return suma

print(suma_lista([1, 1, 2, 1]))