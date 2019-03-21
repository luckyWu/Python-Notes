
from collections import Iterable
"""1. 判断是不是可迭代类型"""

print(isinstance('abc',Iterable))
print(isinstance(123,Iterable))

"""2. 创建一个迭代器"""

class A():
	def __init__(self):
		self.vaule = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self.vaule < 10:
			self.vaule += 1
			return self.vaule
		else:
			raise StopIteration


# a = A()
# print(next(a))
# print(a.__next__())

"""3. 反向迭代"""
a = [1,2,3,4]

# for i in reversed(a):
# 	print(i)

"""4. enumerate"""
s = [1,2,3,4,5,6]
# for index, vaule in enumerate(s):
# 	print(index, vaule) #输出下标和下标对应的值

"""5. 使用zip函数"""

a = [1,2,3]
b = [3,2,4,5]

#zip(a, b) 会生成一个可返回元组 (x, y) 的迭代器，其中 x 来自 a，y 来自 b,一
#旦其中某个序列到底结尾，迭代宣告结束。因此迭代长度跟参数中最短序列长度一致
# for i, j in zip(a,b):
# 	print(i, j)

"""6. 多个有序序列合并成一个有序序列"""

import heapq
a = [1,3,6,22]
b = [2,3,5,7,8]
# for c in heapq.merge(a, b):
# 	print(c)

"""7. 