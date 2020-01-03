#Problem: n is the number of steps in Gary's hike. s is List of  characters that describe his path. 
#U is for moving up and D is for moving down. Above sealevel is mountain and below sea leve is valley
#Print a single integer that denotes the number of valleys Gary walked through during his hike.
def minimumBribes(q):
	count = 0
	for i in range(len(q)):
		if q[i] > i + 3:
			print('Too chaotic')
			return
		for j in range(max(q[i]-2,0),i):
			if q[j] > q[i]:
				count += 1
	print(count)

minimumBribes([2,1,5,3,4])
minimumBribes([2,5,1,3,4])
minimumBribes([5,1,2,3,7,8,6,4])
minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])

'''    count = 0
    arr_comp = q[:]
    for i in range(len(q)):
        #print(q[i],i+1,i+2,i+3)
        if q[i] > i+3:
            print('Too chaotic')
            return
        if q[i]!=i+1:
            for j in range(len(q)):
                #print(q)
                if arr_comp[j] != j+1 and arr_comp[j] > arr_comp[j+1]:
                    temp = arr_comp[j]
                    arr_comp[j] = arr_comp[j+1]
                    arr_comp[j+1] = temp
                    count+=1
    print(count)'''