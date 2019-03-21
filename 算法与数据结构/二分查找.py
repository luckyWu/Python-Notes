def  bin_search(item, key):
	s, e=0, len(item)
	while s <= e:
		mid = (s+e)//2
		if item[mid] == key:
			return mid

		if key > item[mid]:
			s = mid + 1
		else:
			e = mid - 1
	return -1
	

s = [1,2,3,5,7,98]
res = bin_search(s,7)
print(res)

# prices = {
#     'AAPL': 191.88,
#     'GOOG': 1186.96,
#     'IBM': 149.24,
#     'ORCL': 48.44,
#     'ACN': 166.89,
#     'FB': 208.09,
#     'SYMC': 21.29
# }

# dic = {key:value for key, value in prices.items()}
# print(dic)