# The keyword argument end can be used to 
# avoid the newline after the output, or end the output with a different string:


a, b = 0, 1

while a < 1000:
    print(a, end=',')
    a, b = b, a+b