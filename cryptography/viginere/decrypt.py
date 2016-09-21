#!/usr/bin/python
#encrypter
#usage: decrypt.py encrypted.txt decrypted.txt

import os, sys, getpass

def decrypt(line, password): #function takes a line and encrypts it with k char.
    decrypt_message = ""
    a = 0
    for x in line:
        k = password[a%len(password)]
        if ord(x) >= 65 and ord(x) <= 90:
            place = ord(x)-65 #location on alphabet
            place = (place - k)%26
            place += 65
        elif ord(x) >= 97 and ord(x) <= 122:
            place = ord(x)-97 #location on alphabet
            place = (place - k)%26
            place += 97
        else:
            place = ord(x)
        decrypt_message += chr(place)
        a += 1
    return decrypt_message

def key(password): #converts password to list of numbers
    numpass = []
    for x in password.lower():
        numpass.append(ord(x) - 97)
    return numpass

numpass = key(getpass.getpass("enter password: "))
print numpass

encrypted = open(sys.argv[1], 'r').readlines()
decrypted = open(sys.argv[2], 'w')

for x in encrypted:
     decrypted.write(decrypt(x, numpass))
    
decrypted.close()


