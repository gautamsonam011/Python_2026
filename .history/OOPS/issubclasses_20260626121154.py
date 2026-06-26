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

print(bool(re.match('[A-Za-z0-9]+$','abdc1321')))