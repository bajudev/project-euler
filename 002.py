
# n = (n-1) + (n-2)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def calcSum():
    sum = 0
    for i in range(0, 40000):
        if fibonacci(i+1) < 4000000:
            if fibonacci(i+1) % 2 == 0:
                sum += fibonacci(i+1)
                print(sum)
        else:
            break
    return sum

calcSum()