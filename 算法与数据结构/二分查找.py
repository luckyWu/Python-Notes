# def  bin_search(item, key):
# 	s, e=0, len(item)
# 	while s <= e:
# 		mid = (s+e)//2
# 		if item[mid] == key:
# 			return mid

# 		if key > item[mid]:
# 			s = mid + 1
# 		else:
# 			e = mid - 1
# 	return -1
	



def bin_search(item, key):
	s, e = 0, len(item)
	while s <= e:
		mid = (s+e)//2
		if key < item[mid]:
			e = mid-1
		if key > item[mid]:
			s = mid+1
		if key == item[mid]:
			return mid
	return -1
s = [1,2,3,5,7,98]
res = bin_search(s,7)
print(res)