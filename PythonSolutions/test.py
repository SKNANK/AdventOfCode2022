with open('Inputs\day6.txt') as fp:
  input = fp.read()

for i, char in enumerate(str(input)):
  if len(set(input[(i-14):i])) == 14:
    print(i)
    break
  else:
    continue