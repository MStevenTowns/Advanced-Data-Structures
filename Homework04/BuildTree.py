import BinaryTree

def buildTree(list):
	for i in range(0, len(list)):
		if(i==0):
			r=BinaryTree.BinaryTree(list[0])
		elif(i>0 and i%2==0):
			r.insert_left(list[i])
		else:
			r.insert_right(list[i])
	return r

list=[1,2,3,4,5]

r=buildTree(list)

r.inOrder()
print()
r.postOrder()
print()
r.preOrder()
