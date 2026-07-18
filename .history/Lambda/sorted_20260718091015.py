# Syntax 
# sorted(iterable, key=lambda x: expression, reverse=False)

# Q1: Sort a list of numbers 

numbers = [5, 2, 8, 1, 9]

result = sorted(numbers)

print(result)

# Q2: Sort in descending order 

result = sorted(numbers, reverse=True)
print(result)

# Q3 Sort list of tuples by second element

students = [
    ("Rahul", 85),
    ("Sonam", 95),
    ("Amit", 75)
]

result = list(sorted(students, key=lambda x:x[1], reverse=False))
print(result)