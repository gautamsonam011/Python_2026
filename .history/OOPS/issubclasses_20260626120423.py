class Parent(object):
    pass

class Child(Parent):
    pass

print(issubclass(Parent, Child))
print(issubclass(Child, Parent))

obj1 = Child()
obj2 = Parent()

print(isinstance(Child, obj1))
print(isinstance(Parent, obj2))