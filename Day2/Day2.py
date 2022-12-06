#Day 2 AoC

plays = open("Day2\Day2.txt", "r").read().splitlines()
#print(plays)
#print(plays[-2]) all there, just not printed in terminal in vs code

#A is Rock, B is Paper, C is Sci
#X is Rock, Y is Paper, Z is Sci
# 1 point,   2 points,   3 points just for choosing shape respectively
#0 points for lose, 3 points for draw, 6 points for win
    #   R    P    S
opp = ["A", "B", "C"]
you = ["X", "Y", "Z"]

    #opp:you
# Wins R:P (0-1)=-1, P:S (1-2)=-1, S:R (2-0)=2
# Lose P:R (1-0)= 1, S:P (2-1)= 1, R:S (0-2)=-2

# lookup index then math? if win, -1 or -2?, same index = tied, check for warp around, otherwise positive = lose, negative = win
#opp.index - you.index, first check equal, second check warp around

playscut = plays[0:5]
#print(playscut) ## ['C Z', 'A Y', 'C Z', 'A Y', 'C Y']

#commited to checking win based on math and index search, assuming math is quick for single digits and index search in array is quick, maybe enumeration would have been better?

points = 0
for e in playscut:
    moves = e.split()
    #draw condition
    if(opp.index(moves[0]) == you.index(moves[1])):
        #find points based on shape
        points = points + you.index(moves[1]) + 1 # add 1 to the index value of array of moves
        points = points + 3 # add for draw
    #lose condition