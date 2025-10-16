#🌟HERENCIA

class Persona:
    
    def __init__(self, name, estatura:float, age):
        self.name = name
        self.estatura = estatura
        self.age = age
        

class Papa(Persona):
    
    def __init__(self, name, estatura, age):
        super().__init__(name, estatura, age)
        
    def saludo(self):
        
        print(f"Hola soy {self.name}, mi estatura es {self.estatura} y mi edad es {self.age}")
        

papa1 = Papa("Miguel", 1.70, 53)
papa1.saludo()

#🌟FUNCION __LEN__

class Libro:
    
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        
    def __len__(self):
        return self.paginas
    
libro1 = Libro("Coraline", 350)
print(len(libro1))


class Biblioteca :
    
    def __init__(self):
        self.libros = []
        
    def agregar_libros(self, libro):
        self.libros.append(libro)
        
    def __len__(self):
        return len(self.libros)
    
biblio = Biblioteca()
biblio.agregar_libros("Python")
biblio.agregar_libros("Coraline")
print(len(biblio))


class EquipoFutbol:
    
    def __init__(self, jugadores):
        self.jugadores = jugadores
        
    def __len__(self):
        
        return sum(1 for j in self.jugadores if j['titular'])
    
equipos = EquipoFutbol([
    {"nombre": "Ana", "titular": True},
    {"nombre": "Luis", "titular": False},
    {"nombre": "Marta", "titular": True},
])

print(len(equipos))

#🌟EJERCICIOS

class Animal:
    
    def __init__(self, especie, name):
        self.especie = especie
        self.name = name
        
    def sonido(self):
        pass
    
class Gato(Animal):
    
    def __init__(self, especie, name):
        super().__init__(especie, name)
        
    def sonido(self):
        print("Miau")
        
class Perro(Animal):
    
    def __init__(self, especie, name):
        super().__init__(especie, name)
        
    def sonido(self):
        print("Guau!")
    
gato1 = Gato("Gato", "Yumi")
gato1.sonido()
perro1 = Perro("Perro", "Bolt")
perro1.sonido()


#🌟Mini reto

class Empleado:
    
    def __init__(self, name, puesto, salario):
        self.name = name
        self.puesto = puesto
        self.salario = salario
        

class Subgerente(Empleado):
    
    def __init__(self, name, puesto, salario):
        super().__init__(name, puesto, salario)
        
    def ordenando(self):
        print("Ordenando y cuidando")
        

class Vendedor(Empleado):
    
    def __init__(self, name, puesto, salario):
        super().__init__(name, puesto, salario)
        
    def vendiendo(self):
        print("Vendiendo")
        
subgerente1 = Subgerente("Ricador", "Subgerente", 1500)
subgerente1.ordenando()
vendedor1 = Vendedor("Rosa", "Vendedor", 1200)
vendedor1.vendiendo()