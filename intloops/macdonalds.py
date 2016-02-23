#!/usr/bin/python
#macdonalds vs janitor
#wage, pay, balance, total

balance = 0
for pay in range(0,30):
	pay = 2**pay 
	print "Day's pay: $",pay*0.01
	balance = pay + balance
	print "Subtotal: ",balance*.01

