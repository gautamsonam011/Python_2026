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

# Q4: Find minimum

result = reduce(lambda x, y: x if x<y else y, numbers)
print(result)

# Q5: Concatenate strings

words = ["Python", " ", "is", " ", "Awesome"]

result = reduce(lambda x, y: x+y, words)
print(result)

# Q6: Find the longest string 

words = ["Python", "Java", "JavaScript", "C"]

result = reduce(lambda x, y: x if len(x) > len(y) else y, words)
print(result)

# Q7: Sum of salaries 

employees = [
    {"name": "Rahul", "salary": 50000},
    {"name": "Sonam", "salary": 80000},
    {"name": "Amit", "salary": 60000}
]

total_salary = reduce(lambda total, emp: total+emp["salary"], employees, 0)
print(total_salary)

# The third argument (0) is the initial value.

# Q8: Count total characters 

words = ["Python", "Java", "C"]

total_ch = reduce(lambda total, word: total+len(word), words, 0)
print(total_ch)