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

playscut = plays[0:45]
#print(playscut) ## ['C Z', 'A Y', 'C Z', 'A Y', 'C Y']
                    #d      w       d       w       l
#commited to checking win based on math and index search, assuming math is quick for single digits and index search in array is quick, maybe enumeration would have been better?

points = 0
for e in plays: #plays -> playscut for testing, could make calc a seperate function
    moves = e.split()
    #move both win/loss calculation and points per move outside
    movecalc = opp.index(moves[0]) - you.index(moves[1])  #shifting move calculation outside loop
    points = points + you.index(moves[1]) + 1 # add 1 to the index value of array of moves for points based on shape
    ## print(moves[1]) #adding prints to easy calc
    #continues are prob redundant
    #draw condition
    if(movecalc == 0):
        points = points + 3 # add for draw print("d")
        continue
    #lose condition
    elif(movecalc == 1 or movecalc == -2):
        points = points + 0 # not necessary but to make clear nothing should be added on lose print("l")
        continue
    #win condition
    elif(movecalc == -1 or movecalc == 2): 
        points = points + 6 # print("w")
        continue
    else: #throwing simple exception instead of try..
        print("error in calculation, check")
     
#could make calc a function

print(points)

#Part 2 can use difference to find index value.

# x = lose, y = draw, z = win
# 0 , 3, 6 so index * 3
points = 0
for e in plays:
    movecond = e.split()
    # add points from win draw lose
    #print(movecond)
    #print(movecond[1])
    #print(3*you.index(movecond[1]))
    points = points + (3*you.index(movecond[1])) # using you as lose, draw, win instead of move 
    
   
    # add points from their move shifted, based on draw lose win
    # on lose do nothing!!! wrong, still need to add moves
    if (you.index(movecond[1]) == 0):
        yourmove = (((opp.index(movecond[0])) -1 +3) % 3) # forgot to add points based on move that lead to loss
        points = points + yourmove + 1
        #print(yourmove)
        #print("lose")
        continue
    # on draw, same move
    elif (you.index(movecond[1]) == 1):
        points = points + opp.index(movecond[0]) + 1 # adding value of move, index + 1 since moves in order
        #print("draw")
        #print(opp.index(movecond[0]) + 1)
        continue
    elif (you.index(movecond[1]) == 2):
        #print("win")
        #can use modulo 2? shift based on moves index of opponent + 1?
        # r->p, p->s, s->r, 01, 12, 2(3)0
        yourmove = ((opp.index(movecond[0]) + 1) % 3) # move index search based on win condition
        #print(yourmove)
        points = points + yourmove + 1 # don't need to find by index again
        continue
    else: #primitive exception find
        print("error")
print(points)