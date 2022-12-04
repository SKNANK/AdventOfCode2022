import numpy as np
with open("Inputs\day3.txt") as l:
    sacks = [sack.rstrip('\n') for sack in l]

total =0

for x in sacks:
    first  = x[:len(x)//2]
    second = x[len(x)//2:]
    
    for i in first:
        if i in second:
            if i.islower():
                total+=(ord(i)-96)
                break
            else:
                total+=(ord(i)-38)
                break
print(total)

groups = np.array_split(sacks, len(sacks)//3)
newtotal=0

for x in groups:
    for i in x[0]:
        if i in x[1]:
            if i in x[2]:
                if i.islower():
                    newtotal+=(ord(i)-96)
                    break
                else:
                    newtotal+=(ord(i)-38)
                    break

print(newtotal)

