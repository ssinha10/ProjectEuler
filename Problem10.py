# lis = []
# sum = 0


# a = range(0, 2000001)
# for num in a:
# 	print num
# 	if num > 1:
# 		for i in range(2,num):
# 			if(num%i) == 0:
# 				break
# 		else:
# 			lis.append(num)

# #print lis


# for value in lis:
# 	sum += value

# print sum
	

import math, sys

def prime_sieve(maximum):
   
    a = [1 for x in xrange(maximum)]
    a[0] = 0
    a[1] = 0

    
    sievemax = int(math.sqrt(maximum) + 1)

    i = 2
    while (i < sievemax):
        j = i + i
        while j < maximum:
            a[j] = 0
            j += i

      
        while True:
           i += 1
           if a[i] == 1:
               break

    return a

s = prime_sieve(2000000)
print(sum(i for i in xrange(len(s)) if s[i] == 1))










