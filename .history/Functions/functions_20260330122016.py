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

print(ask_ok(prompt='n'))