with open("texto3.txt", "r") as archivo:
    contenido = archivo.read()
    
        
print(contenido)

texto_limpio = contenido.lower().replace(",", "").replace(".", "")
palabras = texto_limpio.split()
contador = {}


for palabra in palabras:
    if palabra in contador:
        
        contador[palabra] += 1
        
    else:
        contador[palabra] = 1
        
top3 = sorted(contador.items(), key=lambda x: x[1], reverse=True)[:3]
with open("texto2", "w") as salida:
    
    salida.write("Las 3 palabras mas usadas son:\n")
    
    for palabra, cantidad in top3:
        salida.write(f"{palabras}: {cantidad}\n")