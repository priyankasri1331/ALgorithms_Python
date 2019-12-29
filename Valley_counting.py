#Problem: n is the number of steps in Gary's hike. s is List of  characters that describe his path. 
#U is for moving up and D is for moving down. Above sealevel is mountain and below sea leve is valley
#Print a single integer that denotes the number of valleys Gary walked through during his hike.
def countingValleys(n, s):
    alt = 0
    alt_prev = 0
    count = 0
    for i in s:
        if i == 'U':
            alt_prev = alt
            alt+= 1
            if alt_prev == -1 and alt == 0:
                count = count + 1
        else:
            alt_prev = alt
            alt-= 1
    return count

count = countingValleys(8,['U','D','D','D','U','D','U','U'])
print(count)