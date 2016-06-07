a = raw_input ()
list2 = []
multiply = 1



T2 = map(int, a)
print len(T2)

for i in range(0,988):



	multiply = T2[i] * T2[i+1] * T2[i+2] * T2[i+3] * T2[i+4] * T2[i+5] * T2[i+6] * T2[i+7]*T2[i+8]*T2[i+9]*T2[i+10] * T2[i+11] * T2[i+12]
 	list2.append(multiply)




print ".........................."
print max(list2) 






