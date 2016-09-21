#!/usr/bin/python
#palindromefx

def ispal(st):
	if st != st[::-1]:
		return False
	return True

word = str(raw_input("enter a string: "))
print ispal(word)

""" #faster way
def ispal(st):
	return st == st[::-1]
"""

"""
def ispalindrome(st): #st can be the same as word
	if st[::-1] == st:
		return (True)
	return (False) #return is always the last line of the function; returns control to global program

word = raw_input()

if ispalindrome(word):
	print word, "is a palindrome"
else:
	print word, "is not a palindrome"
"""
