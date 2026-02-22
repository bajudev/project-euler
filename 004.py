# palindromic
import numbers

def arrayify(num):
    item = str(num)
    number = []
    for i in range(0, len(item)):
        number.append(item[i])
    return number

def palindrome(num):
    item = str(num)
    palindrome = []
    for i in range(len(item) - 1, -1, -1):
        palindrome.append(item[i])
    return palindrome

def checkPalindromic(num):
    if arrayify(num) == palindrome(num):
        return True
    else:
        return False

def products():
    products = []
    for i in range(1, 1000):
        for j in range(1, 1000):
            products.append(i * j)
    products.sort()
    return products

def findPalindromic(products):
    for i in range(len(products) - 1, -1, -1):
        if checkPalindromic(products[i]) == True:
            print(products[i])
            break

findPalindromic(products())


