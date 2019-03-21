def select_sort(items):
	n = len(items)
	for i in range(n-1):
		for j in range(i+1,n):
			if items[i] > items[j]:
				items[i], items[j] = items[j], items[i]
	return items

s = select_sort([3,2,5])
print(s)
