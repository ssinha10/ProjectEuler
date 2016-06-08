 
def trial(n, tracker = 1):
    while n > 1:
        tracker += 1
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
    return tracker
 
max = [0,0]
for i in range(1000000):
    c = trial(i)
    if c > max[0]:
        max[0] = c
        max[1] = i
 
print max[1]