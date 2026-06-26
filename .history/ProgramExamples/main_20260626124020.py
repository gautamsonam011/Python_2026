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

print(unique_number([5, 6, 8, 3, 8, 5]))
print(unique_number([5, 7, 3, 8]))
      
# 3. Write a program for counting the number of every character of a given text file.

# 5. Write a Program to add two integers >0 without using the plus operator.

def add_nums(num1, num2):
    while num2 != 0:
        data =  num1 & num2
        num1 = num1 ^ num2
        num2 = data << 1
    return num1
print(add_nums(2, 10))
