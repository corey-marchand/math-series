__version__ = '0.1.0'

def fibonacci(n):
    a = [0, 1]
    if n < 0:
        print('Incorret input')
    elif n == 0:
        return a[0]
    elif n == 1:
        return a[1]
    else:
        for i in range(2,n+1):
            c = a[0] + a[1]
            a[0] = a[1]
            a[1] = c

        return a[1]


print(fibonacci(9))

def lucas(n):
    a = [2, 1]
    if n < 0:
        print('Incorrect Input')
    elif n == 0:
        return a[0]
    elif n == 1:
        return a[1]
    else: 
        for i in range(2,n+1):
            c = a[0] + a[1]
            a[0] = a[1]
            a[1] = c 

        return a[1]
    
print(lucas(7))

