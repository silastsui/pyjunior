#!/usr/bin/python
#encrypter
#usage: encrypt.py secret.txt encrypted.txt

import os, sys

def encrypt(line, k): #function takes a line and encrypts it with k char.
    secure_message = ""
    for x in line:
        if ord(x) >= 65 and ord(x) <= 90:
            place = ord(x)-65 #location on alphabet
            place = (place + k)%26
            place += 65
        elif ord(x) >= 97 and ord(x) <= 122:
            place = ord(x)-97 #location on alphabet
            place = (place + k)%26
            place += 97
        else:
            place = ord(x)
        secure_message += chr(place)
    return secure_message

secret = open(sys.argv[1], 'r').readlines()
encrypted = open(sys.argv[2], 'w')

for x in secret:
     encrypted.write(encrypt(x, 1))
    
encrypted.close()
