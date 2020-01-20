def countTriplets(arr, r):
    dic = {}
    ls = []

    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                ls.append([i,j,k]) 

    count = 0

    for i in ls:
        #print(i, arr[i[0]],arr[i[1]],arr[i[2]])
        if arr[i[1]] == arr[i[0]]*r and arr[i[2]] == arr[i[0]]*r*r:
            count+=1

    return count



#arr = [1,4,16,64]
arr = [1,2,1,2,4]
arr = [1,3,3,9,9,9,27,81]
#arr = [12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12]
#r = 1
r = 3
a = countTriplets(arr,r)
print(a)