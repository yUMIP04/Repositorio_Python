set1 = {1, 2, 3, 1, 2, 3}

print(set1)

set2 = {5, 6, 7, 8}
set3 = {5, 6, 9, 10}

print(set2.intersection(set3) )

tupla1 = (1, 2, 3, 4, 5)

for numeros in tupla1:
    print(numeros)
    
  
def nombres_unicos():
    nombres = []
    nombres_originales = {} 
    usuario = ""

    
    while usuario != "fin":
        usuario = input("Ingresa nombres: ").lower()
        
        if usuario == "fin":
            break
        nombres.append(usuario)
        
        nombres_originales = set(nombres)
    return nombres_originales
        
        
    
print(nombres_unicos() )