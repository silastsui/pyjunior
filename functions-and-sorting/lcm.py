#!/usr/bin/python
#lcm
#smallest lcm is max(x,y)
#largest lcm is x*y

def mymax(x,y):
	if x > y:
		return x
	return y

def lcm(x,y):
	for i in range(mymax(x,y),x*y+1):
		if i%x == 0 and i%y == 0:
			return i

x = int(raw_input("Enter a number: "))
y = int(raw_input("Enter a number: "))

print lcm(x,y)
