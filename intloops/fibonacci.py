#!/usr/bin/python
#fibonacci sequence

n = int(raw_input("enter a number "))
def fib(n):
	a, b = 0, 1
	for i in range(n):
		a, b = b, a + b
	return a
print fib(n)
