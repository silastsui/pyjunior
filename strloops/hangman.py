#!/usr/bin/python
#hangman

def lettercheck(word, guess, new_letter):
    for x in range(len(word)):
        if new_letter == word[x]:
            guess = guess[:x] + new_letter + guess[x:]
            return "That letter is in the word.", guess
        return "Sorry, that letter is not in the word.", guess

import random

easy = ['special', 'cabbage', 'data', 'country', 
        'ordering', 'factor', 'forever', 'drinking']
medium = ['jacket', 'sexist', 'fish', 'quokka', 
        'bamboozled', 'apply', 'dying', 'extreme']
hard = ['foxy', 'nymph', 'zephyr', 'funky',
        'phlegm', 'jazz', 'lynx', 'buzz']

difficulty = (raw_input("Select your difficulty: (easy/medium/hard) ").lower())
print "Difficulty:", difficulty

word = random.choice(medium)

guess = "_"*len(word)
print guess
 
used_letters = []

while guess != word:
    new_letter = str(raw_input("Guess a letter: "))
    if len(new_letter) > 1:
        print "sorry, you can only type one letter at a time"
    else:
        for x in range(len(word)):
            if new_letter == word[x]:
                guess = guess[:x] + new_letter + guess[x+1:]
        print guess
        used_letters.append(new_letter)
        print "Guessed letters:", used_letters
print "Congratulations! You got the word!"
