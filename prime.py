#!/usr/bin/python

def prime(n):
	status = True
	if n < 2:
		status = False
	else:
		for i in range(2,n):
			if n % i == 0:
				status = False
	return status

for n in range(1,101):
	if prime(n):
		if n == 97:
			print n
		else:
			print n," "
