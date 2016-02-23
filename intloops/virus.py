#!/usr/bin/python
#virus program

infected = 0
day = 0
while infected < 7300000000: 
	infected = 2**day + infected
	day = day + 1
print "The world will end in", day, "days"
