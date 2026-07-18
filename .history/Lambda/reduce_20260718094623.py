# Syntax 
# from functools import reduce

# reduce(function, iterable)

# with lambda 

# from functools import reduce

# reduce(lambda x, y: expression, iterable)

# Q1: Sum of all numbers 

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

result = reduce(lambda x, y: x + y, numbers)
print(result)