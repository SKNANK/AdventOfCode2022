with open("Inputs\day6.txt") as l:
    signals = [signal for signal in l]

signal = signals[0]
tempcheck = []
check=0
numcheck=-1

for i in signal:
    numcheck+=1
    for x in signal[numcheck:]:
        if x in tempcheck:
            tempcheck=[]
            break
        if len(tempcheck) == 13:
            numcheck += 14
            print(numcheck)
        check+=1    
        tempcheck.append(x)
        
