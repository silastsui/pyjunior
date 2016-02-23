#!/usr/bin/python
#guesserprogram

import random
a = range(1,2)
number = int((random.choice(a)))

while True:
    guess = int((raw_input("Guess a number from 1 to 100. ")))
    if guess == 0:
        print "The game will now automatically quit."
        break
    elif guess == number:  
        print "You got the number!"
        break
    elif guess > number:
        print "Your number is too big."
    else:
        print "Your number is too small."
