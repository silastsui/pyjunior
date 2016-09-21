#!/usr/bin/python
#find gcf

def gcf(x,y):
	limit = max(x,y)
	fac=[]
	for i in range(1, limit+1):
		if x%i == 0 and y%i ==0:
			fac.append(i)
	print "The common factors between ",x, "and", y, "are", fac
	print "The greatest common factor is ", max(fac)

x = int(raw_input("Enter a number: "))
y = int(raw_input("Enter a number: "))

gcf(x,y)
