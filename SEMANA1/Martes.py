
usuario = input("Ingresa una frase: ").lower().replace("a", "*").replace("e", "*").replace("i", "*").replace("o", "*").replace("u", "*").split()
contador = 0
lista_palabras = []

for palabra in usuario:
    contador += 1
    lista_palabras.append(palabra)
    
    resultado = "-".join(lista_palabras)
    
    
    if palabra.isdigit():
        
        numeros = int(palabra)
        
        print(f"La frase si tiene numeros y son:{numeros}")
        
    else:
     print("La frase no tiene numeros")
    
print(f"La frase tiene {contador} palabras")
print(resultado)
