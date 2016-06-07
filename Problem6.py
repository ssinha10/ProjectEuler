list = range(0,101)
sumSquare = 0
squareSum = 0
a = 0

for i in list:
	sumSquare += i**2

for j in list:

	a += j
	squareSum = a**2

answer = squareSum - sumSquare

print answer