# Syntax 
# filter(function, iterable)

# with lambda function 

# filter(lambda arguments: expression, iterable) 

# Q1: filter even numbers 

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

result = list(filter(lambda x : x%2 == 0, numbers))
print(result)