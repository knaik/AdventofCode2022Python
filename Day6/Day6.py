#Day 6

text = open("Day6\Day6.txt","r")
signal = text.read().splitlines()[0]
text.close()

#print(signal)
signal = list(signal)
#print(signal)

index = 0
temp = []



print(temp)
for n in range(4,len(signal)):
    temp = []
    temp.append(signal[n])
    temp.append(signal[n+1])
    temp.append(signal[n+2])
    temp.append(signal[n+3])
    temp.append(signal[n+4])
    temp.append(signal[n+5])
    temp.append(signal[n+6])
    temp.append(signal[n+7])
    temp.append(signal[n+8])
    temp.append(signal[n+9])
    temp.append(signal[n+10])
    temp.append(signal[n+11])
    temp.append(signal[n+12])
    temp.append(signal[n+13])
    
    temp = set(temp)
    print(temp)
    if(len(temp) == 14):
        index = n
        print(temp)
        break
    temp = []
print(index+14)

#print(signal[3379-13],signal[3379-13],signal[3379-13],signal[3379-13])