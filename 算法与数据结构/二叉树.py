class BinTNode():
	def __init__(self,data,left=None,right=None):
		self.data = data
		self.left = left
		self.right = right

p = BinTNode(1)
def CreateTree(p):
	ch = input('>>>')
	if ch == '#':
		p = None
		return
	p = BinTNode()
	if not p:
		return
	p.data = ch
	CreateTree(p.left)
	CreateTree(p.right)

	
s = CreateTree(p)