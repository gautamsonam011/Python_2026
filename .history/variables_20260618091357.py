# Public variable :- It is a global variable 

class Public():
    def public_variable(self, a):
        return a
    
obj = Public()
s = obj.public_variable(23)
print(s)  

# Protected variable:- It is a protected variable. Only access or modified by developer. It is presented by using prefix _a 

class Protected():
    def protected_variable(self, _a, b):
        sum = _a+b
        return sum
    
obj1 = Protected()

r = obj1.protected_variable(21, 56)
print(r)

# Private Variable: It is represent with double underscor prefix __a. It can not access and modified. 

class Private():
    def private_variable(self, __a):
        return __a
    
obj2 = Private()
r1 = obj2.private_variable(34) 
print(r1)   

# __init__() 

class Employeedetails():
    def __init__(self, Name, Age, Department):
        self.Name = Name
        self.Age = Age
        self.Department = Department

ob = Employeedetails("Raj", 25, "IT")

print(ob.Name)
print(ob.Department)

# Pass, Break, Continue 

list = [45, 67, 89, 0, 43, 89, 0]

for i in list:
    pass

    if i == 0:
        current = i
        break
    elif i % 2 == 0:
        continue
    print(i)
print(current)    
        
# Slicing 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# syntax :- [start:stop:step]

# Start 

print(numbers[3:])

# stop
print(numbers[:5])

# Step 

print(numbers[2:7:2])

import array

a = array.array('i', [1, 3, 4])
for i in a:
    print(i, end=' ')

# a = array.array('i', [1, 3, "string"])  

# print(a)


temp = 10   # global-scope variable
def func():
     global temp
     temp = 20   # local-scope variable
     print(temp)
func()   

# decorator 

def decorator_func(fun):

    def wrapper():
        print("It is before the function call")
        fun()
        print("It is wrapper function")

    return wrapper()

@decorator_func
def hello():
    print("Hello world")  

list = [56, 78, 53, 23] 

x = [sum(list)]
print(x)

squared_dict = {x:x**2 for x in list if x%2 != 0}
print(squared_dict)

# Assigning lambda functions to a variable:

mul = lambda a, b: a*b

print(mul(4, 5))

# Wrapping lambda functions inside another function:
def wrapp_lambda(n):
    return lambda a: a*n

mult = wrapp_lambda(6)
print(mult(2))

from copy import copy, deepcopy
list_1 = [1, 2, [3, 5], 4]
## shallow copy
list_2 = copy(list_1) 
list_2[3] = 7
list_2[2].append(6)
print(list_2)    # output => [1, 2, [3, 5, 6], 7]
list_1    # output => [1, 2, [3, 5, 6], 4]
## deep copy
list_3 = deepcopy(list_1)
list_3[3] = 8
list_3[2].append(7)
print(list_3)    # output => [1, 2, [3, 5, 6, 7], 8]
list_1    # output => [1, 2, [3, 5, 6], 4]

 