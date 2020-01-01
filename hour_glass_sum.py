#Problem: This problem returns max value of hour glass sum
def leftrot(a,d):
	loc_arr = []
	for i in range(len(A)):
		for j in range(len(A[i])):
			if (not((i-1)<0)) and (not((j-1)<0)) and (not((i+1)>=len(A))) and (not((j+1)>=len(A[i]))):
				#print(i,j)

			#print(A[i+1][j+1])
			#if ([i-1][j+1] and [i-1][j-1] and [i+1][j+1] and [i+1][j-1] and [i+1][j] and [i-1][j]):
				loc_arr.append(A[i][j] + A[i-1][j+1] + A[i-1][j-1] + A[i+1][j+1] + A[i+1][j-1] + A[i+1][j] + A[i-1][j])
	return max(loc_arr)

a = [1, 1, 1, 0, 0, 0]
print(HourGlassSum(a,3))