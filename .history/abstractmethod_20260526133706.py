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

# a = Animal()
# Because Animal has an abstract method.

# 2. Child class must implement abstract methods

class Cat(Animal):
    pass 

# c = Cat()

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class Razorpay(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using Razorpay")

obj = Razorpay()
print(obj.pay())

class PayPal(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using PayPal")

obj1 = PayPal()
print(obj1.pay())        