from Node import *

class UnorderedList:
	def __init__(self):
		self.head=None
	def isEmpty(self):
		return self.head==None
	def add(self, item):
		temp=Node(item)
		temp.set_next(self.head)
		self.head=temp
	def size(self):
		current=self.head
		count=0
		while current!=None:
			count=count+1
			current=current.get_next()
		return count
	def search(self, item):
		current=self.head
		fount=False
		while current !=None and not found:
			if current.getData()==item:
				fount=True
			else: 
				current=current.getNext()
		return found
	def remove(self, item):
		current=self.head
		previous=None
		fount=False
		while not found:
			if current.getData()==item:
				found=True
			else:
				previous=current
				current=current.getNext()
		if previous==None:
			self.head=current.getNext()
		else:
			previous.setNext(current.getNext())
			
