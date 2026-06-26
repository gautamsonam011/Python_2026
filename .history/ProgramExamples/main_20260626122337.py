# 1. Write python function which takes a variable number of arguments.

def variable_number(*arg):
    for i in arg:
        print(i)

obj = variable_number((3, 5, 6, 7)) 
      
