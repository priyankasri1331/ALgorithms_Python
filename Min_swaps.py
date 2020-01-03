#Given an array [1,2,....n], unsorted, finding the minimum number of swaps required to sort it in ascending order

def minimumSwaps(arr):
	arr = [arr[i]-1 for i in range(len(arr))]
	arr_dict = {}

	for ind,val in enumerate(arr):
		arr_dict[ind] = val

	visited = [0 for i in range(len(arr))]
	cycle_length = 0
	count = 0



	for j in range(len(arr)):

		if visited[j] == 1:
			continue

		if visited[j]!= 1 and arr_dict[j]!=j:
			count+=1

		while(visited[j] != 1):
			visited[j] = 1
			if arr_dict[j] != j:
				cycle_length+=1
				j = arr_dict[j]

	return (cycle_length-count)


#print(minimumSwaps([1, 3, 5, 2, 4, 6, 7]))
#print(minimumSwaps([4, 3, 1, 2]))
#print(minimumSwaps([7,5,3,2,1,4,6]))
print(minimumSwaps([1,3,4,5,2,7,5]))
