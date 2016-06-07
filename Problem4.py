# count = 0
# for i in xrange(999, 100, -1):
# 	for j in xrange (999, 100, -1):
# 		x = i * j
# 		if x > count:
# 			s = str(i*j)
# 			if s == s[::1]:
# 				count = i * j
# print count

# def is_palindrome(num):
#     return str(num) == str(num)[::-1]

# def fn(n):
#     max_palindrome = 1
#     for x in range(n,1,-1):
#         for y in range(n,x-1,-1):
#             if is_palindrome(x*y) and x*y > max_palindrome:
#                 max_palindrome = x*y
#             elif x * y < max_palindrome:
#                 break
#     return max_palindrome

# print fn(999)

list = []

for i in range(100, 999):
    for j in range(100, 999):
        num = i * j
        if str(num) == str(num)[::-1]: #Check if the reverse is the same as the forward
            list.append(num)

print(max(list))




