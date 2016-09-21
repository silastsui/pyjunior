#!/usr/bin/python
#hiddenpalindrome

word = raw_input("Enter the word: ")

def search():
    for x in range(len(word),1,-1):
        for i in range(len(word)+1-x):
            phrase = word[i:i+x]
            if phrase == phrase[::-1]:
                return len(phrase)
    return 1
            
print search()
