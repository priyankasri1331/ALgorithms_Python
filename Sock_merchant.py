#n: the number of socks in the pile
#ar: the colors of each sock
#Outputting the number of pairs of socks that are matching

def sockMerchant(n, ar):
    temp_dict ={}
    var = 0
    for i in ar:
        temp_dict[i] = 0

    for i in ar:
        temp_dict[i] += 1

    for j in temp_dict:
        var += int(temp_dict[j]/2)
    
    return var

var = sockMerchant(9,[10, 20, 20, 10, 10, 30, 50, 10, 20])
print(var)

