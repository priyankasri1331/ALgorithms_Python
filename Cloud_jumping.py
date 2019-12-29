#c is an array of binary integers indicating the dangerous(1) and normal clouds(0). Atmost 2 steps jump possible.
#Outputting least number of jumps

c = [0,1,0,1,0,1,0,0,0,0,0,0,0,0,1,0,1,0, 0,0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0]
#c = [0,1,0,0,1,0]
#c = [0, 0, 0, 1, 0, 0]
steps = 0
i = 0
while(i < len(c)-1):
    if ((i + 2) < len(c)) and c[i+2] != 1:
        steps += 1
        i = i + 2
        #print('2 steps:')
        #print(i)
    else:
        steps += 1
        i = i + 1
        #print('1 step:')
        #print(i)
print(steps)
