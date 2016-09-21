#!/usr/bin/python
#wordlength2

sent = str(raw_input("Enter a sentence:"))
wCount = 0
for x in range(len(sent)):
	if sent[x:] == " ":
		wCount += 1
	else:
		continue
print "There are",a+1,"words in this sentence."
