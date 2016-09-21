#!/usr/bin/python
#alphabet

#ord stands for ordinal
#chr stands for character

ualph = ""
for x in range(ord("A"),ord("Z")):
	ualph += chr(x)
print ualph

lalph = ""
for x in range(ord("a"),ord("z")):
	lalph += chr(x)
print lalph
