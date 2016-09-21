#!/usr/bin/python
#encrypter
#usage: encrypt.py encrypted.txt decrypted.txt

import os, sys

def decrypt(line, k): #function takes a line and encrypts it with k char.
    decrypt_message = ""
    for x in line:
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
    return decrypt_message

encrypted = open(sys.argv[1], 'r').readlines()
decrypted = open(sys.argv[2], 'w')

for x in encrypted:
     decrypted.write(decrypt(x, 1))
    
decrypted.close()

