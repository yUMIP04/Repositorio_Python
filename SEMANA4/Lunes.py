import requests
import json



#🌟EJERCICIO CON POKEAPI GET

response = requests.get("https://pokeapi.co/api/v2/berry-firmness/1/")
datos = response.json()
print(datos['name'])

#🌟POST

post_prueba = "https://jsonplaceholder.typicode.com/todos"
datos = {"name": "Victoria"}
response2 = requests.post(post_prueba, data=datos)
print(response2.json())


#🌟PUT

url = "https://jsonplaceholder.typicode.com/posts/1"
datos1 = {
    "id": 1,
    "title": "Ttitulo actualizado",
    "body": "Contenido actualizado",
    "userID": 1
}
response3 = requests.put(url, json=datos1)
print("Codigo:", response3.status_code )
print(response3.json())

#🌟DELETE

url2 = "https://jsonplaceholder.typicode.com/posts/1"
response4 = requests.delete(url2)
print(response4.status_code)


#🌟Mini-reto

for i in range(3):
    
    pokemon= input("Ingresa el id de 3 pokemon: ")
    
    
    poke_api =  requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")
    datos_pokemon = poke_api.json()
    
    print("Nombre:", datos_pokemon['name'])
    print("Peso:", datos_pokemon['weight'])
    print("Tipo:", datos_pokemon["types"][0]["type"]["name"]) 