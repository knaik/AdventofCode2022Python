#Day 3 Aoc

text = open("Day3\Day3.txt", "r")
sacks = text.read().splitlines()
text.close()


sackscut = sacks[0:6]
#print(sackscut)

""" sum = 0
for singlesack in sacks:
    midpt = len(singlesack)//2
    splitone = sorted(singlesack[:midpt]) #close index not inclusive? split
    print(splitone)
    splittwo = sorted(singlesack[midpt:])
    print(splittwo)
    pointerone = 0
    pointertwo = 0
    prior = 0



    while (splitone[pointerone] != splittwo[pointertwo]):  ##no error checking, bad but expect to always find match
        print(splitone[pointerone])
        print(splittwo[pointertwo])
        if (splitone[pointerone] < splittwo[pointertwo]):
            pointerone += 1 
        elif(splitone[pointerone] > splittwo[pointertwo]): # AGHHHHH error for a while because forgot to switch sign
            pointertwo += 1
        else:
            print("error2")#exceptiontwo
            
        if(pointerone > midpt or pointertwo > midpt): #simple exception
            print("error")
        if (splitone[pointerone] == splittwo[pointertwo]):
            #found
            foundchar = splitone[pointerone]
            if (foundchar.isupper()):
                prior = ord(foundchar) - 64 + 26 #get priority based on unicode char value ## add 26 to upper to get right number
            else:
                prior = ord(foundchar) - 96
            print(foundchar)
            break
        if (splitone[pointerone] == splittwo[pointertwo]):
            #found
            foundchar = splitone[pointerone]
            if (foundchar.isupper()):
                prior = ord(foundchar) - 64 + 26
            else:
                prior = ord(foundchar) - 96
            print(foundchar)
            break
    

    if (splitone[pointerone] == splittwo[pointertwo]):
        foundchar = splitone[pointerone]
        if (foundchar.isupper()):
            prior = ord(foundchar) - 64  + 26 #get priority based on unicode char value
        else:
            prior = ord(foundchar) - 96
        print(foundchar)
        print(prior)
        sum = sum + prior
        continue

    print(prior)
    sum = sum + prior
print(sum)
 """

#part 2, can't use part 1 code effectively, easier to find new algorithm, two pointer method can be extended to 3 pointer, and is probably good algorithmic complexity
# but three pointer method is hard

# first remove duplicates in each group of 3? then find intersection?
#what is star arg *arg, *set??

def removeDup(str):
    return "".join(set(str))


#print(sackscut)

deduped = []

for e in sacks: #changes order
    deduped.append(sorted(removeDup(e))) # sorted creates list of list instead of just list of strings of each sack, splitting by letter

#print(deduped) 

n = 0
arr = []
for n in range(0, len(deduped) , 3):
    arr.append( "".join(set(deduped[n]).intersection(deduped[n+1]).intersection(deduped[n+2])))

print(arr)

sum = 0
for k in arr:
    if (k.isupper()):
        print(k)
        sum = sum + ord(k) - 64 + 26
    else:
        print(sum)
        sum = sum + ord(k) - 96

print(sum)