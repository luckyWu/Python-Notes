


def parting(item, start=0, end):
	n = end
	key = item[start]
	for i in range(n):
		if item[i] < key:
			k = item.pop(i)
			item.insert(0,k)
	index = item.index(key)
	return item, index


print(parting([44,213,13,4,32,12,34,45],end=7))


