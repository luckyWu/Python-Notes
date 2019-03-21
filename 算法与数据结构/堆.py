class Stack():
	"""堆栈"""
	def __init__(self, max_size):
		self.max_size = max_size
		self.arr = []

	def counts(self):
		return len(self.arr)

	def push(self, item):
		if len(self.arr) == self.max_size:
			print('数据已满，不能存')
			return None
		self.arr.insert(0, item)
		print('存入成功')

	def pull(self):
		if self.counts() == 0:
			print('空栈，不能弹出！！')
			return None
		return self.arr.pop()

	def full(self):
		if len(self.arr) == self.max_size:
			print('Full!')
		else:
			print('Not Full!!')

	def index_of(self, index):
		return self.arr[index]

	def replace(self, index, item):
		self.arr[index] = item
		print('修改成功！')

	def delete(self, index):
		del self.arr[index]
		print('删除成功！！')


s = Stack(5)
s.counts()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.pull()
s.pull()
s.pull()
s.pull()
s.pull()
s.pull()
print(s.counts())

