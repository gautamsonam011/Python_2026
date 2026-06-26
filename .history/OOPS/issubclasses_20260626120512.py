class Parent(object):
    pass

class Child(Parent):
    pass

print(issubclass(Parent, Child))
print(issubclass(Child, Parent))

obj1 = Child()
obj2 = Parent()

print(isinstance(obj1, Parent))
print(isinstance(obj2, Parent))