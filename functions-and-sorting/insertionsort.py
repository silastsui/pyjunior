#!/usr/bin/python
#insertionsort

import random

old = random.sample(xrange(100000),10)
print old

def inssort(seq):
    new = [min(old)-1] #creates a list with a small arbitrary number 
    for x in range(len(old)):
        for i in range(len(new), -1, -1): #goes through the new list
            if seq[x] > new[i-1]: #checks if number from old list is bigger 
                new.insert(i,seq[x]) #if next number is bigger, insert number before it
                break
    new.pop(0) #get rid of your small arbitrary number
    return new

def inssort2(seq):
    current = 1
    while current < len(seq):
        for i in range(current):
            if seq[current] < seq[i]:
                seq[i],seq[current] = seq[current],seq[i]
        current += 1
    return seq
    
print inssort(old)
