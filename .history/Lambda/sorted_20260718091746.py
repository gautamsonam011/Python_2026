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

result = list(sorted(students, key=lambda x:x[1], reverse=True))
print(result)

# Q4: Sort by name

result = list(sorted(students, key=lambda x:x[0]))
print(result)

# Q5: Sort dictionary by value

marks = {
    "Rahul": 70,
    "Sonam": 95,
    "Amit": 80
}

result = sorted(marks.items(), key=lambda x:x[1])
print(result)

# Q6: Sort list of dictionaries by salary

employees = [
    {"name": "Rahul", "salary": 50000},
    {"name": "Sonam", "salary": 80000},
    {"name": "Amit", "salary": 60000}
]

result = sorted(employees, key=lambda x: x["salary"])

print(result)