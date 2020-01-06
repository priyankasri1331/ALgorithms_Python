#Problem: Two strings are anagrams of each other if the letters of one string can be 
#rearranged to form the other string. Given a string, find the number of pairs of 
#substrings of the string that are anagrams of each other.
def sherlockAndAnagrams(s):
	ana_dict = {}
	list_1 = []
	list_2 = []
	list_3 = []
	count =0 

	for i,sub_st in enumerate(s):
		for j in range(i+1,len(s)+1):
			k = s[i:j]
			#print(i,j,k)
			list_1.append(k)

	print(list_1)

	for i in list_1:
		list_2.append(sorted(i))


	print(list_2)

	for i in list_2:
		list_3.append(''.join(i))

	print(list_3)

	for i in list_3:
		if i not in ana_dict:
			ana_dict[i] = 1
		else:
			ana_dict[i] += 1




	print(ana_dict)

	for i in ana_dict:
		count += ana_dict[i]*(ana_dict[i]-1)/2

	return int(count)

print(sherlockAndAnagrams('abba'))