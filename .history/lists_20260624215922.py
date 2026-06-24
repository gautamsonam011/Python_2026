list = ["app", "web", "soft", "hello"]
print(list[1])

print(list[-1])

print(list[1:3])

if "soft" in list:
    print("Yes")

list[2] = "rak"
print(list)    

# insert() 

list.insert(1, "wait")
print(list)

list.append("shii")
print(list)

tropical = ["mango", "pineapple", "papaya"]
list.extend(tropical)
print(list)

# remove()

list.remove("shii")
print(list)

# pop()

list.pop(1)
print(list)

list.pop()
print(list)

# del keyword 

del list[0]
print(list)

for i in range(len(list)):
    print(i)

# clear() 

# list.clear()
# print(list)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = []

for i in fruits:
    if "a" in i:
        newlist.append(i)

print(newlist)        

newlist = [ i for i in fruits if "a" in i]
print(newlist)

newlist = [i for i in fruits if i != "apple"]
print(newlist)

newlist = [x.upper() for x in fruits]

print(newlist)

# sort()

list.sort()
print(list)