class Parent(object):
    pass

class Child(Parent):
    pass

print(issubclass(Parent, Child))
print(issubclass(Child, Parent))

obj1 = Child()
obj2 = Parent()

print(isinstance(obj2, Parent))
print(isinstance(obj2, Child))

st = "abdc1321"

res = st.isalnum()
print(res)

import re

print(bool(re.match('[A-Za-z0-9]+$','abd&@c1321')))


# Encapsulation 

class Person:
    def __init__(self, __age, name):
        self.__age = __age
        self.name = name

    def details(self):
        print("Details of person", self.name, self.__age)    

obj = Person(45, "Raj")

obj.details()