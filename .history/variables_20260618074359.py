# Public variable :- It is a global variable 

class Public():
    def public_variable(self, a):
        return a
    
obj = Public()
s = obj.public_variable(23)
print(s)    