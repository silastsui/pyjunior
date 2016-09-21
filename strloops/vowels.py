#!/usr/python
#vowels



vow = "aeoiu"
sen = lower_(raw_input("enter something"))
count = 0
for let in sen:
	if let in vow:
		count += 1
print count
	
