# Measure some strings 

words = ['Cow', 'Cat', 'Window', 'Rain', 'House']

for w in words:
    print(w, len(w))

# Create a sample collection 

users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status  
# print(users)

# range() function :
# If you want to iterate sequence with confirm point then use this 

for i in range(10):
    print(i)

# range() and len() 

arr1 = [67, 75, True, 'Python']

for i in range(len(arr1)):
    print(i, i[arr1])