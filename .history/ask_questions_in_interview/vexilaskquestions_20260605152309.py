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


# write a program find out unique items from list

lst = [45, 67, 53, 78, 45, 67]

unique_list = []
for item in lst:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)

lis = []
for item in lst:
    if lst.count(item) == 1:
        lst.append(lis)
        print(lis)