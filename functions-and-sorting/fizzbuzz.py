#!/usr/bin/python
#buzzfizz

#div by 3, fizz, div by 5, fizzbuzz

for x in range(101):
	if x%3 == 0 and x%5 == 0:
		print "fizzbuzz"
	elif x%5 == 0:
		print "buzz"
	elif x%3 == 0:
		print "fizz"
	else:
		print x
