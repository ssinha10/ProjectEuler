# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder
# What is the smalles positive number that is evenly divisible by all of the
# numbers from to to 20.

def findSmallestMultiple(n):
    i = n
    while i < factorial(n):
        if isMultiple(i, n):
            return i
        i += n
    return -1

def isMultiple(x, n):
    for i in range(1, n):
        if x % i != 0:
            return False
    return True

def factorial(n):
    if n > 1: return n * factorial(n - 1)
    elif n >= 0: return 1
    else: return -1

print (findSmallestMultiple(20))