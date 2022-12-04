with open("Inputs\day4.txt") as l:
    sections = [section.rstrip('\n') for section in l]
pp = True
shii = False
total = 0
for i in sections:
    x = i.split(',')
    y = x[0].split('-')
    z = x[1].split('-')
    seq1 = range(int(y[0]), int(y[1])+1)
    seq2 = range(int(z[0]), int(z[1])+1)
    pp = True
    shii = False
    count1 = 0
    count2 = 0
    for n in seq1:
        if n in seq2:
            total+= 1
            break
            
print(total)

    