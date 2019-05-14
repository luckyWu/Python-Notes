def Bubble_sort(items):
	"""冒泡排序"""
	n = len(items)
	for i in range(n-1):
		for j in range(n-i-1):
			if items[j] > items[j+1]:
				items[j], items[j+1] = items[j+1], items[j]
	return items



def Bubble_sort1(items):
	"""冒泡排序改进版"""
	n = len(items)
	for i in range(n-1):
		swap = True
		for j in range(n-i-1):
			if items[j] > items[j+1]:
				items[j], items[j+1] = items[j+1], items[j]
				swap = False
		if swap:
			break
	return items

	
s = Bubble_sort1([1,2,23,4563,23])
print(s)


def mp(items):
	n = len(items)
	for i in range(n-1):
		swap = False
		for j in range(n-i-1):
			if items[j] > items[j+1]:
				items[j+1], items[j] = items[j], items[j+1]
				swap = True
		if not swap:
			break
	return items
print(mp([1,3,2,11,2,4,88,4]))