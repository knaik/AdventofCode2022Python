#Day 2 AoC

plays = open("Day2\Day2.txt", "r").read().splitlines()
#print(plays)
#print(plays[-2]) all there, just not printed in terminal in vs code

#A is Rock, B is Paper, C is Sci
#X is Rock, Y is Paper, Z is Sci

opp = ["A", "B", "C"]
you = ["X", "Y", "Z"]

# lookup index then math? if win, -1 or -2?, same index = tied, check for warp around, otherwise positive = lose, negative = win
#opp.index - you.index, first check equal, second check warp around

