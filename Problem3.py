a = 600851475143
j = 2
while j * j < a:
	while a % j == 0:
		a = a / j
	j += 1
print a
