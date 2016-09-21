#!/usr/bin/python
#euclid's gcf

def gcf(x,y):
	while True:
		r = x % y
		x = y
		y = r
		if r == 0:
			return y
		
	
x = int(raw_input("Enter a number: "))
y = int(raw_input("Enter a number: "))

x1 = x
y1 = y

if y > x:
	x,y = y,x

print "The greatest common factor of",x1,"and",y1,"is",gcf(x,y)
