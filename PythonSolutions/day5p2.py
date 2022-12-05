with open("Inputs\day5.txt") as l:
    moves = [move.rstrip('\n') for move in l]
with open("Inputs\day52.txt") as e:
    sections = [section.rstrip('\n') for section in e]

for i in moves:
    temp = []
    full = i.split(',')
    for _ in range(int(full[0])):
        temp.insert(0, sections[int(full[1])-1][-1])
        sections[int(full[1])-1] = sections[int(full[1])-1][:-1]
    for x in temp:
        sections[int(full[2])-1] = sections[int(full[2])-1] + x

print(sections)
        
