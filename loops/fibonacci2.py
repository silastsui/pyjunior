a,b = 0,1

for x in range(10):
	print a
	temp = b
	b = a + b
	b = temp
