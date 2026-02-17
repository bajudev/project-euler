
# below 100
# multiple of 3 or 5
# multiples of both (multiples of 15)
# check for 15, then check for 3 and 5
# sum the multiples

n = 1000

def calcSum(n):
    sum = 0
    for i in range(0, n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

print(calcSum(n))

