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