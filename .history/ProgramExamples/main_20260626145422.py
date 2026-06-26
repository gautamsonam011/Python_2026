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
    # while num2 != 0:
    #     data =  num1 & num2
    #     num1 = num1 ^ num2
    #     num2 = data << 1
    # return num1
    num1 = num1 ^ num2
    return num1
print(add_nums(2, 10))

# 7. Write a Program to match a string that has the letter ‘a’ followed by 4 to 8 'b’s.

import re

def rematch(data_str):
    pattern = 'ab{4, 8}'

    if re.search(pattern, data_str):
        return "match found"
    else:
        return "match not found"
    
print(rematch("abc")) 
print(rematch("aabbbbbc"))   

# 8. Write a Program to convert date from yyyy-mm-dd format to dd-mm-yyyy format.

from datetime import datetime

new_datetime = datetime.strptime("2021-08-01", "%Y-%m-%d").strftime("%d-%m-%Y")
print(new_datetime)

# 9. Write a Program to combine two different dictionaries. While combining, if you find the same keys, you can add the values of these same keys. Output the new dictionary

from collections import Counter

d1 = {'key1': 50, 'key2': 100, 'key3':200}
d2 = {'key1': 200, 'key2': 100, 'key4':300}

new_dict = Counter(d1)+Counter(d2)
print(new_dict)

for i in range(1, 5):
    print(i)

# for i in xrange(1,10):
#     print(i)