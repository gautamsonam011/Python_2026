students = {
    "Sonam": [85, 90, 78],
    "Rahul": [75, 88, 92],
    "Priya": [95, 89, 91]
}

# Calculate total marks for each student
result = {}

for name, marks in students.items():
    result[name] = sum(marks)

print(result)