#!/usr/bin/python
#votingprogram

citizen = raw_input("Are you a Canadian citizen? (yes/no) ")

if citizen.lower() == "yes":
	age = int(raw_input("How old are you? "))
	if age < 1:
		print "You are not born yet."
	elif age < 18:
		print "You are too young to vote."
	elif age > 120:
		print "You are probably dead."
	else:
		print "You are eligible to vote in Canada!"
else: 
	print "Sorry, you are not eligible to vote in Canada."




