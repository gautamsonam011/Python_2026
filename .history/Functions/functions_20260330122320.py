def fib(n):
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a+b

    print()

fib(100)

# Default Argument Values: 

def ask_ok(prompt, retries = 4, reminder = 'Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'nop', 'nope'}:
            return False
        retries = retries

        if retries < 0:
            raise ValueError('invalid user response')
        
        print(reminder)

# print(ask_ok(prompt='n'))

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
print(f(4))

# Keyword Arguments: 

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])