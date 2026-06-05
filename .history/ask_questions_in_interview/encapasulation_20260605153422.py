class Employee:
    def __init__(self, name, salary):
        self.name = name          # Public variable
        self.__salary = salary    # Private variable

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Salary must be positive")

# Create object
emp = Employee("Sonam", 50000)

# Access through methods
print(emp.get_salary())   # 50000

emp.set_salary(60000)
print(emp.get_salary())   # 60000

# Encapsulation is an OOP concept that binds data and 
# methods into a single unit (class) and restricts direct 
# access to data using private variables. In Python, private 
# variables are created using double underscores (__). We access 
# and modify them through getter and setter methods.

# What is OOPs?

# OOPs (Object-Oriented Programming System) is a programming
#  paradigm that organizes code using objects and classes.
#  It helps make code reusable, maintainable, and scalable.

# Abstraction:

# Hiding implementation details and showing only essential features.

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car Started")

car = Car()
car.start()

# what is session in django?
# how to create tokens in django?