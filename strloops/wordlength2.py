#!/usr/bin/python
#wordlength2

sent = str(raw_input("Enter a sentence:"))
wCount = 1
for x in range(len(sent)):
	print sent[x-1]
	if sent[x-1] != " " and sent[x] == " ":
		wCount += 1
print wCount
sent[x]

