#!/usr/bin/python
#find gcf

def gcf(x,y):
	for i in range(1, max(x,y)+1, -1):
		if x%i == 0 and y%i ==0:
			return i
	
x = int(raw_input("Enter a number: "))
y = int(raw_input("Enter a number: "))

print gcf(x,y)
