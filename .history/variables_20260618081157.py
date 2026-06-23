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