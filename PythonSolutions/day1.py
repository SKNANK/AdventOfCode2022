
""" Puzzle 1
 from itertools import groupby
with open("Inputs\day1.txt") as l:
    elves = [elf.rstrip('\n') for elf in l]
splitelf = [list(g) for k, g in groupby(elves, key=bool) if k]
final = []
for i in splitelf:
    final.append(sum([int(x) for x in i]))

print(max(final)) """

from itertools import groupby
with open("Inputs\day1.txt") as l:
    elves = [elf.rstrip('\n') for elf in l]
splitelf = [list(g) for k, g in groupby(elves, key=bool) if k]
final = []
for i in splitelf:
    final.append(sum([int(x) for x in i]))

topthree = 0
for _ in range(3):
    topthree += max(final)
    final.remove(max(final))

print(topthree)