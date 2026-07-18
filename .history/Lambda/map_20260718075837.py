# Syntax
# map(function, iterable)

# when using lambda function 

# map(lambda arguments: expression, iterable) 

# Q1: Double each number 

numbers = [1, 2, 3, 4, 5, 6]

result = list(map(lambda x: x*2, numbers ))
print(result)

# Q2: Square of each numbers 

square = list(map(lambda x : x**2, numbers))
print(square)

# Q3: Convert strings to uppercase 

name = ["python", "java", "php", "nodejs", "dotnet"]

result_name = list(map(lambda name: name.upper(), name))

print(result_name)

# Q4: Add two lists

list1 = [3, 5, 6, 7, 8]
list2 = [2, 4, 9, 1, 3]

add_list = list(map(lambda x, y: x+y, list1, list2))
print(add_list)

# Q5: Get string lengths 

lengths = list(map(lambda name: len(name), name))
print(lengths)