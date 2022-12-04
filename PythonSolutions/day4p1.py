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
        if pp == True:
            if shii == False:
                if n in seq2:
                    count1 += 1
                    if count1 == (int(y[1])+1 - int(y[0])):
                        shii = True
                        total += 1
                else:
                    for m in seq2:
                        if m in seq1:
                            count2 += 1
                            if count2 == (int(z[1])+1 - int(z[0])):
                                shii = True
                                total += 1
                        else:
                            pp = False
                            break
            
print(total)

    