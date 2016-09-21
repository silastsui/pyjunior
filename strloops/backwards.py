#!/usr/bin/python
#backwards

text = str(raw_input("Enter a phrase: "))

#solution1 (wat)
print text[::-1]

#solution2 (for x in range)
reverse = ""
a = len(text)
for x in range(len(text)-1, -1,-1):
	reverse += text[x]
print reverse


#solution3 (for let in text)
backwards = ""
for let in text:
	backwards = let + backwards
print backwards

#solution4 (reverse)
def reverse(text):
	if len(text) <= 1:
			return text
	return reverse(text[1:]) + text[0]
print reverse(text)

#solution5
reverse = ""
for x in reversed(text):
	reverse += x
print reverse
