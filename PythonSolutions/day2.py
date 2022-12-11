with open("day2.txt") as t:
     strats = [strat.rstrip('\n') for strat in t]

total = 0

def interpreter(moves):
    if moves[0] == 'A':
        return rock(moves)
    elif moves[0] == 'B':
        return paper(moves)
    elif moves[0] =='C':
        return sciss(moves)
    else:
        return None

def rock(moves):
    if moves[2] == 'X':
        return 3
    elif moves[2] == 'Y':
        return 4
    elif moves[2] == 'Z':
        return 8

def paper(moves):
    if moves[2] == 'X':
        return 1
    elif moves[2] == 'Y':
        return 5
    elif moves[2] == 'Z':
        return 9

def sciss(moves):
    if moves[2] == 'X':
        return 2
    elif moves[2] == 'Y':
        return 6
    elif moves[2] == 'Z':
        return 7




for i in strats:
    total += interpreter(i)

print(total)