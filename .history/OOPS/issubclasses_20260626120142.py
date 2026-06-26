class Parent(object):
    pass

class Child(Parent):
    pass

print(issubclass(Parent, Child))
print(issubclass(Child, Parent))
