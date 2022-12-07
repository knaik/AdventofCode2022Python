#Day 5

#stacks and queues

#only stacks actually

arr = ["DTRBJLWG",
"SWC",
"RZTM",
"DTCGSPV",
"GPTLDZ",
"FBRZJQCD",
"SBDJMFTR",
"SBDJMFTRLHRBTVM",
"QPDSV"]

""" move1 = [[1,3,5]] """

#move1 = []

text = open("Day5\Day5.txt","r")
move1 = text.read().splitlines()
text.close()
#print(move1[0])

move2 = []
for e in move1:
    move2.append(e.split(","))


#print(move2)
#stack using list


arrstack = []
for e in arr[0]:
    arrstack.append(e)

#print(arrstack)

arr2 = []

for j in arr:
    arr2.append([char for char in j])

""" print(arr2[1])
print(arr2[2])
k = arr2[1].pop()
arr2[2].append(k) # there is no push
print(arr2[1])
print(arr2[2]) """

#print(arr2)

#print(type(move2[0][0])) string


## part 1
""" 
for move in move2:
    #print(int(move[0]))
    #print(arr2[int(move[1]) - 1])
    #print(arr2[int(move[2]) - 1])
    for i in range(0,int(move[0])):
        k = arr2[int(move[1]) - 1].pop()  ## error assuming 0 index instead of 1 index 
        arr2[int(move[2]) - 1].append(k)
    #print(move)
    #print(arr2[int(move[1]) - 1])
    #print(arr2[int(move[2]) - 1])
#print(arr2)

for el in arr2:
    print(el.pop(), end="")
 """
""" 
print(arr2)
print(move2) """

##part 2, can I use a temporary stack?

##not working
""" temp = []
for move in move2:
    #print(int(move[0]))
    #print(arr2[int(move[1]) - 1])
    #print(arr2[int(move[2]) - 1])
    for i in range(0,int(move[0])):
        k = arr2[int(move[1]) - 1].pop()  ## error assuming 0 index instead of 1 index 
        ##  ##arr2[int(move[2]) - 1].append(k)
        temp.append(k)
    print(arr2[int(move[2]) - 1])
    arr2[int(move[2]) - 1] = arr2[int(move[2]) - 1]+ temp
    print(temp)
    print(arr2[int(move[2]) - 1])
    #print(move)
    #print(arr2[int(move[1]) - 1])
    #print(arr2[int(move[2]) - 1])
#print(arr2)
 """

 ##array splice should work  #1,3,5
for move in move2:
    print(arr2)
    print(move)
    slicelen = int(move[0])
    indxfrom = int(move[1])-1
    indxto = int(move[2])-1
    #print(indxfrom,indxto)
    #print(slicelen)
    #print(int(move[1]))
    #print(arr2[int(move[1])-1])
    #print(arr2[int(move[2])-1])
    cuts = arr2[indxfrom][:-1*slicelen]
    print(cuts)
    del arr2[indxfrom][-1*slicelen]
    print(type(list(cuts)))
    arr2[indxto] = arr2[indxto] + list(cuts)
    print(arr2[indxto])
    print(arr2[indxfrom])
    #print(arr2)
