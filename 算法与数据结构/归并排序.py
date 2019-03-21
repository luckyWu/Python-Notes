def merge(item1, item2):
	"""合并两个序列第一种方法"""
	i = j = 0
	new = []
	while i < len(item1) and j < len(item2):
		if item1[i] < item2[j]:
			new.append(item1[i])
			i = i+1
		else:
			new.append(item2[j])
			j = j+1
	new += item1[i:]
	new += item2[j:]

	return new


def merge1(item1, item2):
	"""合并两个序列第2种方法"""
	new = item1+item2
	new.sort()
	return new


def merge_sort(item):
	"""归并排序"""
	if len(item) <2 :
		return item[:]
	mid = len(item)//2
	l = merge_sort(item[:mid])
	r = merge_sort(item[mid:])
	return merge1(l,r)


# import time

# import random
# alist = [x for x in range(10000)]
# start = time.time()
# s = merge_sort(alist)
# # print(s)
# end = time.time()

# print (end-start)























