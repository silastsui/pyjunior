#!/usr/bin/python
#bubblesort

import random

old = random.sample(xrange(1,100000),10000)

def bubsort(list):
    count = 0
    while count != len(old)-1: 
        count = 0
        for x in range(len(old)-1):
            if old[x] > old[x+1]:
                old[x], old[x+1] = old[x+1], old[x]
            else:
                count += 1
    return old
    
print bubsort(old)
