#!/usr/bin/python
#marriedprogram

name = raw_input("What is your last name? ")
sex = raw_input("What sex are you? (m/f) ")

if sex.lower() == "m":
	mar = raw_input("Are you married? (y/n) ")
	if mar == "y":
		a = "Mr."
	else:
		a = "M."
else:
	mar = raw_input("Are you married? (y/n) ")
	if mar == "y":
		a = "Mrs."
	else:
		a = "Ms."

print "Hello ",a, name
