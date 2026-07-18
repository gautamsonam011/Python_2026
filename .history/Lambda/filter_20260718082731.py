# Syntax 
# filter(function, iterable)

# with lambda function 

# filter(lambda arguments: expression, iterable) 

# Q1: filter even numbers 

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

result = list(filter(lambda x : x%2 == 0, numbers))
print(result)

# Q2: Filter positive numbers 

numbers = [-5,-2,0,4,8,-1,6]

result = list(filter(lambda x: x > 0 , numbers))
print(result)

# Q3: Filter strings with length greater than 5 

names = ["Rahul","Amit","Sonam","Alexander"]

result = list(filter(lambda name : len(name) > 5, names))
print(result)

# Q4: Numbers greater than 50 

numbers = [10,25,60,75,30,90]

result = list(filter(lambda x : x > 50, numbers))
print(result)

# Q5: Filter names starting with 'S' 

names = ["Sonam","Rahul","Shiv","Amit","Sohan"]

result = list(filter(lambda name: name.startwith("S"), names))
print(result)