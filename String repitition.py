#This functin returns the number of 'a' in a repeated infinite string of upto n
def repeatedString(s, n):
    count = 0
    count_2 = 0
    for i in s:
        if i == 'a':
            count+=1
        else:
            continue
    num_of_rep = int(n/len(s))

    last_part_num = n%len(s)


    for i in s:
        if last_part_num > 0:
            if i == 'a':
                count_2+=1
                last_part_num-=1
            else:
                last_part_num-=1
        else:
            break

    num = count*num_of_rep + count_2


    return num

b = repeatedString('aba',10)
print(b)
