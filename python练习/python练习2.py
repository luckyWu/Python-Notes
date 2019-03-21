# person_num = 50
# count = 17
# lists = [0]*person_num
# counter = 0
# i = 0
# while lists.count(0)>1:
# 	if lists[i] == 0:
# 		counter += 1
# 	if counter == count:
# 		lists[i] = 1
# 		# print(lists,i)
# 		counter = 0	
# 	i += 1
# 	i = i % (person_num)

# print(lists)
# print(lists.index(0))


lis = [1,2,[1,2,3,[12,2,3,[4,3,2],5],6],7,[1,2,3,[12,2,3,[4,3,[12,[2],2],2],5],6]]
k = 0
def f(lis):
	global k
	for li in lis:
		if isinstance(li,list):
			k += 1
			f(li)
	return k
print(f(lis))


class BBD():
	def __enter__(self):
		print('enter')

	def __exit__(self,exc_type, exc_val, exc_tb):
		print('end')

with BBD() as f:
	print('----------------')


import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(2, nums)[1]) # Prints [42, 37, 23]# Prints [-4, 1, 2]

def d(items: list) -> int:
	if isinstance(items, list):
		maxd = 1
		for item in items:
			maxd = max(d(item)+1,maxd)
		return maxd
	return 0

print(d(lis))
import time
import timeit

timeit.timeit('[x for x in range(100000000)]',number=1)
# s = time.time()
# k = [0]*1000000000
# e  =time.time()
# print(e-s)



