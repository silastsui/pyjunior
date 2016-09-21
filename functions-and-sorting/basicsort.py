L = ['foxy', 'nymph', 'zephyr', 'funky', 'phlegm', 'jazz', 'lynx', 'buzz', 'cwm', 'syzygy']
#print sorted(L)

L.sort()
#print L

def wordlen(w):
    return len(w)

L = ['ted', 'john', 'benjamin', 'annabelle']

a = L[:]
a.sort()
print a

L.sort(key = wordlen)
print L

for item in L:
    print item
    
for x in range(len(L))
    print L[x]
    
