""".
Polimorfismo(Multiples Formas): Nace de la herencia, crear multiples formas, dependiendo el objeto que se debe ir formando, interactua de manera diferente con la misma variable

"""

class Animal:
    def speak(self):
        pass
    
class Dog(Animal):
    def speak(self):
        print("Guau guau")
        
class Cat(Animal):
    def speak(self):
        print("Miau miau")
        
#crear instancia o objetos

dog = Dog()
dog.speak()
cat = Cat()
cat.speak()