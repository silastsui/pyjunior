#!/usr/bin/python
#magicsquares

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")
line4 = raw_input("Line 4: ")

def row(n):
    total = 0
    for x in square[4*n-4:4*n]:
        total = total + int(x)
    return total

def column(n): 
    total = 0
    for x in square[n-1:16:4]: 
        total = total + int(x)
    return total

def magic():
    number = row(1)
    for x in range(1,5):
        if row(x) and column(x) != number:
            return "not magic"
    return "magic"

square = line1 + " " + line2 + " " + line3 + " " + line4
square = square.split()

print magic()  
