#!/usr/bin/python
#encrypter
#usage: encrypt.py secret.txt encrypted.txt

import os, sys, getpass

def encrypt(line, password): #function takes a line and encrypts it with k char.
    secure_message = ""
    a = 0
    for x in line:
        k = password[a%len(password)]
        if ord(x) >= 65 and ord(x) <= 90:
            place = (((ord(x)-65) + k)%26 + 65)
        elif ord(x) >= 97 and ord(x) <= 122:
            place = (((ord(x)-97) + k)%26 + 97)
        else:
            place = ord(x)
        secure_message += chr(place)
        a += 1
    return secure_message

def key(password): #converts password to list of numbers
    numpass = []
    for x in password.lower():
        numpass.append(ord(x) - 97)
    return numpass

numpass = key(getpass.getpass("enter password: "))
        
secret = open(sys.argv[1], 'r').readlines()
encrypted = open(sys.argv[2], 'w')

for x in secret:
     encrypted.write(encrypt(x, numpass))
    
encrypted.close()
