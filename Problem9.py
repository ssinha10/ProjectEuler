a = range(500)
b = range(500)
c = range(500)


for x in a:
	
	for y in b:
		
		for z in c:
			
			if(x**2 + y**2 == z**2 and x < y < z):
				if(x + y + z == 1000):
					print x, y, z
					print x * y * z



