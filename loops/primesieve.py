#!/usr/bin/python
#prime

import math

print 2
for x in range(3,101,2):
	prime = True
	for y in range(2, int(math.sqrt(x)+1)):
		if x % y == 0:
			prime = False
			break
	if prime == True:
		print x

"""
print 2
for x in range(3,101,2):
	if all(x%i != 0 for i in range(2,int(math.sqrt(x))+1)):
		print x
"""
