number = 10001
i = 2
count = 0
prime = 0
now = []

while count < number:

    for x in range (2,i+1):
        if len(now) == 2:
            break
        elif i%x == 0:
            now.append(x)

    if len(now)==1:
        prime = i
        count += 1
    now = []
    i+=1       



print(prime)