# 1. Write python function which takes a variable number of arguments.

def variable_number(*arg):
    for i in arg:
        print(i)

variable_number(45)

# 2. WAP (Write a program) which takes a sequence of numbers and check if all numbers are unique.

def unique_number(data_list):
    if len(data_list) == len(set(data_list)):
        return True
    return False

unique_number([5, 6, 8, 3, 8, 5])
      
