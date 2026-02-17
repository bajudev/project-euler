
# let n = a natural number
# to find prime factors:
# check all values 0 to n where i is any value in that range
# if i % n = 0
#   for j in range 1 to i+1
#       if i % j = 0
#           if j = i
#               return true

def primeFactors(n):
    primes = []
    denominator = 2
    while n > 1:
        if n % denominator == 0:
            primes.append(denominator)
            n = n // denominator
        else:
            denominator += 1
    return primes[len(primes)-1]

print(primeFactors(600851475143))