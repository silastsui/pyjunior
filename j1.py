#!/usr/bin/python
#tournamentselection

game1 = raw_input("Game 1 Result: ")
game2 = raw_input("Game 2 Result: ")
game3 = raw_input("Game 3 Result: ")
game4 = raw_input("Game 4 Result: ")
game5 = raw_input("Game 5 Result: ")
game6 = raw_input("Game 6 Result: ")

score = game1 + game2 + game3 + game4 + game5 + game6

count = 0
for x in score.lower():
    if x == "w":
        count += 1

if count >= 5:
    print 3
elif count >= 3:
    print 2
elif count >= 1:
    print 1
else:
    print -1
