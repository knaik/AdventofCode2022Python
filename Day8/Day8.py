import numpy as np


text = open("Day8\Day8.txt", "r")
trees = np.array([list(x.strip()) for x in text], int) #don't want to use normal array, not really big enough
text.close()


#print(trees)

gridone = np.zeros_like(trees, int)
#print(gridone) #initialize zero

for j in range(1):
    for x,y in np.ndindex(trees.shape):   # for each x,y coordinate do
        """  print(x,y)
        print(trees[x, y+1:])
        print(trees[x, y]) """
        less = trees[x, y+1:] < trees[x, y] #count when smaller
        #print(less)
        gridone[x,y] = gridone[x,y] | all(less)
        #print(all(less))  #bitwise or operator
    trees, gridone = map(np.rot90, [trees, gridone]) #rotate with map
"""     print(trees)
    print(gridone) """

print(gridone.sum())



gridtwo = np.ones_like(trees, int)
#print(gridtwo)

for k in range(4):
    for x,y in np.ndindex(trees.shape):   
        lower = trees[x, y+1:] < trees[x, y]
        gridtwo[x,y] *= next((i+1 for i,t in enumerate(lower) if ~t), len(lower))
    trees, gridtwo = map(np.rot90, [trees, gridtwo])

print(gridtwo.max())