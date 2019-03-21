import itertools



def main():
	"""全排列"""
	a = itertools.permutations('ABCD')
	for val in a:
		print(val)
	"""组合"""
	b = itertools.combinations('abcde', 3)
	for val in b:
		print(val)
	"""笛卡尔积"""
	b = itertools.product('♠♥♣♦', range(1,14))
	for val in b:
		print(val)

def PrimeIter(object):
	"""素数迭代器"""

	def __init__(self,min_val=2,max_val):
		self.min_val = min_val-1
		self.max_val = max_val

	def is_prime(num):
		for f in range(2, int(sqrt(num))+1):
			if num % f == 0:
				return False
		return True

	def __iter__(self):
		return self

	def __next__(self):
		self.min_val += 1
		while self.min_val <= self.max_val:
			if is_prime(self.min_val):
				return self.min_val
			self.min_val += 1
		raise StopIteration()

for i in PrimeIter(10):
	print(i)







# if __name__ == '__main__':

	# main()