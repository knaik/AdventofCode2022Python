#Day 1 of Advent of Code

day1input = open('Day1.txt', 'r')
day1arr = day1input.readlines()
#print(day1arr)

index = 0
totalitems = day1arr.count("\n")


lst = []
temp = 0

for  e in day1arr:
    if(e == "\n"):
        lst.append(int(temp))
        temp = 0
        continue
    temp = temp + int(e.strip())

lst.append(int(temp))

#print(lst)

#print(max(lst)) ## max works one, sort is easiest way to get max in order

#more optimal way is to do single traversal and keeping index values
#fast is either to sort and then return first second third index or remove max element and call max() three times

lst.sort(reverse=True)
print(sum(lst[:3]))

#print(lst[0]+lst[1]+lst[2])
#print(lst)

#print(lst[-1]+lst[-2]+lst[-3])