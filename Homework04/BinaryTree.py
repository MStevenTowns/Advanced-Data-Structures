class BinaryTree:
	def __init__(self,root):
		self.key=root
		self.left=None
		self.right=None
		
	def insert_left(self,newNode):
		if self.left==None:
			self.left=BinaryTree(newNode)
		else:
			t=BinaryTree(newNode)
			t.left=self.left
			self.left=t
			
	def insert_right(self,newNode):
		if self.right==None:
			self.right=BinaryTree(newNode)
		else:
			t=BinaryTree(newNode)
			t.right=self.right
			self.right=t
			
	def getVal(self):
		return self.key
		
	def getLeft(self):
		return self.left

	def getRight(self):
		return self.right

	def setVal(self,obj):
		self.key=obj
		
	def preOrder(self):
		print(self.getVal())
		if self.left:
			self.left.preOrder()
		if self.right:
			self.right.preOrder()

	def postOrder(self):
		if self.left:
			self.left.postOrder()
		if self.right:
			self.right.postOrder()
		print(self.getVal())

	def inOrder(self):
		if self.left:
			self.left.inOrder()
		print(self.getVal())
		if self.right:
			self.right.inOrder()
