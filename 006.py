# The sum of the squares of the first 10 natural numbers = 385
# The square of the sum of the first 10 natural numbers = 3025
# Hence the difference between the sum of the squares of the first 10 natural numbers and the square of the sum is 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# We know that the sum of the squares of the first n natural numbers = 1/6(n)(n+1)(2n+1)
# And the square of sum of the first n natural numbers = ((n)(n+1)/2)^2

def differenceOfSquares(n):
    sumOfSquares = (n*(n+1)*((2*n)+1))/6
    squareOfSum = ((n*(n+1))/2)**2
    return squareOfSum - sumOfSquares

num = int(input("Enter the number to find its difference of squares: "))
print(differenceOfSquares(num))