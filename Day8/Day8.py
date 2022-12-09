import numpy as np

text = open("Day8\Day8.txt", "r")
trees = np.array([list(x.strip()) for x in text], int) #can't use normal array, not big enough
text.close()


print(trees)