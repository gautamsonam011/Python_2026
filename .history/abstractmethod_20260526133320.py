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

# Important Points 

# 1. Abstract class cannot be instantiated 

a = Animal()
# Because Animal has an abstract method.