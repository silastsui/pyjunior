#!/usr/bin/python
#encrypter
#usage: decrypt.py encrypted.txt decrypted.txt

import os, sys, getpass, itertools, string

def decrypt(line, password): #function takes a line and encrypts it with k char.
    decrypt_message = ""
    a = 0
    for x in line:
        k = password[a%len(password)]
        if ord(x) >= 65 and ord(x) <= 90:
            place = (((ord(x)-65) - k)%26 + 65) #location on alphabet
        elif ord(x) >= 97 and ord(x) <= 122:
            place = (((ord(x)-97) - k)%26 + 97)
        else:
            place = ord(x)
        decrypt_message += chr(place)
        a += 1
    return decrypt_message

def key(password): #converts password to list of numbers
    numpass = []
    for x in password:
        numpass.append(ord(x) - 97)
    return numpass

keylength = int(raw_input('keylength: '))
alphabet = list(string.ascii_lowercase)
popwords = ['and', 'the', 'can', 'with', 'from', 'have', 'how', 'can'
            'then', 'also', 'that', 'for', 'you', 'not', 'but', 'are']

encrypted = open(sys.argv[1], 'r').readlines()
decrypted = open(sys.argv[2], 'w')

for x in itertools.permutations(alphabet, keylength):
    numpass = key(x) #turns permutation key into 
    for n in encrypted:
        if any(word in decrypt(n,numpass) for word in popwords): #only checks single lines...
            decrypted.write(str(x))
            decrypted.write(decrypt(n, numpass))
        
decrypted.close()
