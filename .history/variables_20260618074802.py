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

