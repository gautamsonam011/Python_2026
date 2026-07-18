# Syntax
# map(function, iterable)

# when using lambda function 

# map(lambda arguments: expression, iterable) 

# Q1: Double each number 

numbers = [1, 2, 3, 4, 5, 6]

result = list(map(lambda x: x*2, numbers ))
print(result)