import math

lis = []
for k in range(1, 76576501): 
	a = (k*(k+1))/2

	lis.append(a)
#print lis
#lis is the list of all the triangular numbers

# cnt = 0
# answer = 0
# cnt = []
# for i in lis:
# 	#print i
# 	b = range(2, (i+1))
# 	#print b
# 	for number in b:
# 		del cnt[:]
# 		if (i % number == 0):
# 			cnt.append(number)
# 			print cnt

c = []
print lis
for number in lis:
	
	b = range(2, number+1)
	#b is all the numbers from 2 to the number
	for i in b:
		if (number % i == 0):
			c.append(i)
			if (len(c) == 499):
				print number
				break
	del c[:]


	








			




		
#print count
	





# def factors(number):
#     factors = {1}
#     for i in range(2, int(math.sqrt(number)) + 1):
#         if number % i == 0:
#             factors.add(i)
#             factors.add(number / i)
#     return factors


# if __name__ == "__main__":
#     number_of_divisors = 0
#     start_number = 1000
#     triangular_number = 0
#     while number_of_divisors < 501:
#         triangular_number = sum(range(1, start_number))
#         number_of_divisors = len(factors(triangular_number))
#         start_number += 1
#     print(triangular_number)