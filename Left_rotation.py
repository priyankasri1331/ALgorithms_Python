#Problem: This problem returns max value of hour glass sum
def rotLeft(a, d):
			
	return a[d:] + a[:d]



A = [1 ,2 ,3 ,4 ,5]
print(rotLeft(A, 4))

#    for i in range(d):
#        temp = a[0]
#        for j in range(len(a)-1):
#            a[j] = a[j+1]
#       a[len(a)-1] = temp
            
#    return a
