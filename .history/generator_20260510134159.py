def fibbo(n):
    p, q = 0, 1
    while(p < n):
        yield p
        p, q = q, p+q

x = fibbo(10)

x.__next__()

for i in fibbo(10):
    print(i)

def multiply(a, b, *argv):
   mul = a * b
   for num in argv:
       mul *= num
   return mul
print(multiply(1, 2, 3, 4, 5))    

