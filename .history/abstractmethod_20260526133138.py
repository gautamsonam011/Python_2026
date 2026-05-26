from abc import ABC, abstractmethod

# Abstract class 

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

# Child class 

class Dog(Animal):

    def sound(self):
        return "Bark"

# Object Creation 

d = Dog()
print(d.sound())        