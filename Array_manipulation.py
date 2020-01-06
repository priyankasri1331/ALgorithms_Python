#Starting with a 1-indexed array of zeros and a list of operations,
#for each operation add a value to each of the array element between two given indices, 
#inclusive. Once all operations have been performed, return the maximum value in your array.
def arrayManipulation(n, queries):
	arr = [0 for i in range(n)]

	for ind,lis in enumerate(queries):

		a,b,k = lis

		arr[a-1] += k
		arr[b] -= k
	print(arr)

	total = 0
	maximum = 0


	for ind,val in enumerate(arr):

		total += val
		maximum = max(total,maximum)

	return maximum




queries = [[1,2,100],[2,5 ,100],[3, 4, 100]]
#queries = [[1,5,3],[4,8 ,7],[6, 9, 1]]
#queries = [[2 ,6, 8],[3, 5, 7],[1, 8, 1],[5, 9, 15]]
g = arrayManipulation(10,queries)
print(g)



