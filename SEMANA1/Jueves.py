amigos = {
  
    "Juan" : 23,
    "Victor": 30,
    "Lupe": 13
}


amigos.update({"Victoria": "21"})
print(amigos)

for name,edad in amigos.items():
    print(f"{name} : {edad}")
    
    
def contador_palabras():
    
    usuario = input("Ingresa una frase: ").lower().replace(",", "").replace(".", "")
    contador_palabra = {}
    
    for palabra in usuario.split():
        
        if palabra in contador_palabra:
            contador_palabra[palabra] += 1
            
        else:
            contador_palabra[palabra] = 1
            
    return contador_palabra

print(contador_palabras())