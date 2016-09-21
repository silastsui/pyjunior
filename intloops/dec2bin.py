#!/usr/bin/python
#dec2bin converter

def dec2bin(num):
    bin = []
    while num != 0:
        bin.insert(0,num%2)
        num = num / 2
    new = 0
    for x in range(len(bin)):
        new = new + bin[len(bin)-1-x]*(10**x)
    return new

num = int(raw_input("Enter a decimal number: "))
print dec2bin(num)
