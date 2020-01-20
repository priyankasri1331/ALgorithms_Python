from itertools import permutations


def countTriplets(arr, r):
    l = len(arr)
    ls1 = []
    for i in range(l):
        ls1.append(i)

    perm = permutations(ls1,3)
    #print(list(perm))

    count = 0

    for i in list(perm):
        #print(i, arr[i[0]],arr[i[1]],arr[i[2]])
        if i[0] < i[1] and i[1] < i[2] and arr[i[1]] == arr[i[0]]*r and arr[i[2]] == arr[i[0]]*r*r:
            count+=1
            print(i)

    return count
#arr = [1,4,16,64]
arr = [1,2,1,2,4]
#arr = [12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12]
#r = 1
r = 2
a = countTriplets(arr,r)
print(a)