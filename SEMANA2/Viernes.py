#🌟POO

class MyClass:
    x = 5
    
p1 = MyClass()
print(p1.x)

#🌟METODO ___INIT___()

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
p2 = Person("John", 52)
print(p2.name)
print(p2.age)

#🌟METODO __STR__()

class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name}({self.age})"

p3 = Person2("John", 36)
print(p3)

#🌟CREAR METODOS


class Perro:
    
    def __init__(self, tipo, sexo):
        self.tipo = tipo
        self.sexo = sexo
        
    def myfunc(self):
        print(f"Mi perro es de raza {self.tipo} y es {self.sexo}")
        
perro1 = Perro("FreshPull", "Hembra")
perro1.myfunc()

#🌟HERENCIA

class Persona:
    
    def __init__(self, name, lname):
        self.name = name
        self.lname = lname
        
    def imprimir(self):
        print(f"{self.name} {self.lname}")
        
x = Persona("Victoria", "Perez")
x.imprimir()    

class Mujer(Persona):
    def __init__(self, name, lname, year):
        super().__init__(name, lname)
        self.year = year
        
    def imprimir_bienvenida(self):
        print(f"Bienvenido {self.name} {self.lname}")
        
y = Mujer("Aome", "Figurashi", "2019")
y.imprimir()
y.imprimir_bienvenida()

#🌟ITERADORES

"""
🌟ITER
"""

tupla = ("appel", "banana", "cherry")
myit = iter(tupla)

print(next(myit))
print(next(myit))
print(next(myit))

class Numeros():
    
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        
      if self.a <= 20:  
        x = self.a
        self.a += 1
        return x
      else:
       raise StopIteration
    

    
myclass = Numeros()
iterador = iter(myclass)

for z in iterador:
    print(z)
    
    
#🌟ACTIVIDADES

class Persona1:
    
    def __init__(self, name:str, edad:int):
        self.name = name
        self.edad = edad
        
    def saludar(self):
        print(f"Hola soy {self.name} y tengo {self.edad} de edad.")
        
person1 = Persona1("Victoria", 21)
persona2 = Persona1("Aome", 12)
persona3 = Persona1("Juan", 22)
person1.saludar()
persona2.saludar()
persona3.saludar()

#🌟MIIRETO

class Gato:
    
    def maullar(self):
        print("Miau!")
        
    def comer(self):
        print("Comiendo...")
        
gato1 = Gato()
gato1.maullar()
gato1.comer()