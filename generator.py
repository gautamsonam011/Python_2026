def fibbo(n):
    p, q = 0, 1
    while(p < n):
        yield p
        p, q = q, p+q

x = fibbo(10)

x.__next__()

for i in fibbo(10):
    print(i)

def multiply(a, b, *argv):
   mul = a * b
   for num in argv:
       mul *= num
   return mul
print(multiply(1, 2, 3, 4, 5))    

def tellArguments(**kwargs):
   for key, value in kwargs.items():
       print(key + ": " + value)
tellArguments(arg1 = "argument 1", arg2 = "argument 2", arg3 = "argument 3")

class Parent(object):
   pass   
 
class Child(Parent):
   pass   

print(issubclass(Child, Parent))    
print(issubclass(Parent, Child))

import pandas as pd
dataframe = pd.DataFrame( data, index, columns, dtype)