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

# Q7: Sort by age (descending) 
employees = [
    {"name": "Rahul", "age": 25},
    {"name": "Sonam", "age": 30},
    {"name": "Amit", "age": 22}
]

result = sorted(employees, key=lambda x: x["age"], reverse=True)

print(result)

# Q8: Sort strings by length 
words = ["Python", "C", "Java", "JavaScript"]

result = sorted(words, key=lambda x: len(x))

print(result)

# Q9: Sort by last character 

words = ["apple", "banana", "kiwi", "orange"]

result = sorted(words, key=lambda x: x[-1])

print(result)

# Q10: Sort by multiple keys

employees = [
    {"name": "Rahul", "age": 25, "salary": 50000},
    {"name": "Sonam", "age": 25, "salary": 80000},
    {"name": "Amit", "age": 22, "salary": 60000}
]

result = sorted(
    employees,
    key=lambda x: (x["age"], x["salary"])
)

print(result)