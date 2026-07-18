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

# Q2: Product of numbers

result = reduce(lambda x, y: x*y, numbers)
print(result)

# Q3: Find maximum

result = reduce(lambda x, y: x if x > y else y, numbers)
print(result)