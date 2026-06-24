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