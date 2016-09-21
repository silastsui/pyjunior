#!/usr/bin/python
#selection sort

import random

old = random.sample(xrange(1,100000),10000)

def selsort(list): 
    new = []
    while old != []: #can also use len(old) != 0, but not as efficient
        small = old[0]
        for x in old:
            if x < small:
                small = x
        new.append(small)
        old.remove(small)
    return new

def selsort2(list): 
    new = []
    while old != []:
        new.append(min(old))
        old.remove(min(old))
    return new

print selsort(old)

#types of sorting
#selection sort, insertion sort, merge sort, quick sort

#other method for creating old
"""
old = []
for x in xrange(10000):
    old.append(random.choice(range(100000)))
"""
