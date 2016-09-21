#!/usr/bin/python
#bin2dec converter

def bin2dec(num):
    power = len(num)-1
    dec = 0
    for x in num:
        dec = dec + int(x)*(2**power) 
        power -= 1
    return dec

num = raw_input("Enter a binary number: ")
print bin2dec(num)
