#Day 4

text = open("Day4\Day4.txt","r")
ids = text.read().splitlines()
text.close()

idscut = ids[0:8]

#print(idscut)

count = 0
for e in ids:
    bothe = e.split(",")
    #print(bothe)
    first = bothe[0].split("-")
    #print(first)
    second = bothe[1].split("-")
    #print(second)
    """ if(first[0] == second[0] and first[1] == second[1]):
        count += 1
        continue
    elif(first[0] >= second[0] and first[1] <= second[1]):
        count += 1
        continue
    elif(first[0] <= second[0] and first[1] >= second[1]):
        count += 1
        continue
    else:
        continue """


        # I don't know why the top logic doesnt work
    
    #first inside second, 2-3 in 1-4
    if (int(second[0]) - int(first[0]) <= 0 and int(second[1]) - int(first[1]) >= 0):
        count = count + 1
        #second inside first, 1-4, 2-3
    elif (int(second[0]) - int(first[0]) >=0 and int(second[1]) - int(first[1]) <=0 ):
        count = count + 1
    elif (first[0] == second[0] and first[1] == second[1]):
        count = count + 1
    else:
        continue

##print(count) 

# too lazy to comment out logic, so unecessary calculations

#part 2

# test if endpoints exist between the endpoints of second?

count2 = 0
for e in ids:
    bothe = e.split(",")
    #print(bothe)
    first = bothe[0].split("-")
    #print(first)
    second = bothe[1].split("-")
    #print(second)

