# remove 2 from list 

l = [1, 2, 2, 4, 6, 7]

for i in l:
    if i == 2:
        l.remove(i)

print(l)   

print([i for i in l if i != 2])

# check none  

a = None

if a is None:                 # == check the value if you use is then it is check identity
    print("a is none")

a = "Apple"
b = "Orange"

print(f"{a} and {b} both are healthy fruits")


# what output of this 

if []:                      # [], "" blank it's mean false so if condition is false 
    print("yes")
else:
    print("no")     # output is no


if "":
    print("yes")
else:
    print("no")  #output no

if " ":
    print("yes")
else:
    print("no")  #output yes   


# find a string 

lst = ["I", "am", "learning", "python"]

print(" ".join(lst))

# square print another list 
# beg

list1 = [1, 2, 3, 4, 5]

result = []

for i in list1:
    result.append(i*i)

print(result)    

# Or 
# Pro 
list2 = [1, 2, 3, 4, 5]
result = list(map(lambda x: x*x, list2))

print(result)

print(0 or 5)    # 0 consider false so print 5
print("" or "Hello")  # "" consider false so print Hello

# merge and create a seperate according to student 

name = ['Ankur', 'Chaman', 'Ishank']

bed = ["w1", "w2", "w3"]

fee_status = ["paid", "paid", "unpaid"]

all_details = list(zip(name, bed, fee_status))
print(all_details)

# output 

nums = [False, False, True]     # all() use for check that all value are true if all values are true then print True if not then print false
print(all(nums))

  
num = [1, 2, 3, 4]
num.remove(2)
num.pop(1)

print(num)


