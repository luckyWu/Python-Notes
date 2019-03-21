# z = {'a':1,'b':2}
# x, y = z
# print(x, y)


# k = [1,2,3,4,5,6,7,8,9]
# x , *_ , y = k
# print(x, y)

# k1 = [1,2,3,4,5,('a','b','c', 'd')]
# x, *y, (*_, z) = k1
# print(x, y, z)

# from collections import deque
# q = deque(maxlen=3)
# q.append(1)
# q.append(2)
# q.append(3)
# q.append(4)
# # q.append(5)
# # q.append(6)
# # q.append(7)
# # q.append(8)
# # q.append(9)
# print(q)


# import heapq
# nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
# print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]

from collections import OrderedDict,Counter

# d = OrderedDict()
# d['a'] = 1
# d['b'] = 22
# print(d)
# d['c'] = 1
# print(d)

# items = [1,2,3,4,5]
from functools import reduce
# a = reduce(lambda x,y:x+y,map(lambda x:x**2,items[::2]))
# print(a)

# items1 = [1000,1000,2000,2000,2001,2034]
# k = 0
# for i in Counter(items1).most_common():
# 	if i[1]>1:
# 		k += 1
# print(k)
# i= 1
# while i:
# 	k = 7*i
# 	if (k+1)%2 ==0 and (k+2)%3==0 and (k+4)%5==0 and (k+5)%6==0:
# 		break
# 	i += 1
# print(7*i)

def five(k1):
	try:
		a = reduce(lambda x,y:x+y,map(lambda x: int(x)**2, list(str(k1))))
		if a == 1:
			print(':快乐树')
			return  
		five(a)
	except:
		print(':不是快乐树')
		return  	

five(37)
if (0) in {1,0,2,3}:
	print('ok')

