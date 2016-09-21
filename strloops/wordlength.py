#!/usr/bin/python
#wordlength

sent = str(raw_input("Enter a sentence:"))
wCount = 1
cCount = 0
for x in sent:
	if x == " ":
		wCount += 1
print "Words:",wCount


