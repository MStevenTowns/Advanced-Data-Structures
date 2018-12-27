class Node:
    def __init__(self, initData):
        self.data=initData
        #self.next=None
        self.parent=None
        self.right=None
        self.left=None
    def getData(self):
        return self.data
    #def getNext(self):
    #    return self.next
    def setData(self, newData):
        self.data = newData
    #def setNext(self, newNext):
     #   self.next=newNext
    def getParent(self):
        return self.parent
    def getRight(self):
        return self.right
    def getLeft(self):
        return self.left
    def setParent(self,p):
        self.parent=p
    def setRight(self,r):
        self.right=r
    def setLeft(self,l):
        self.left=l
    
    def insert(self, val):
        if val<self.getData():
            if self.getLeft()==None:
                self.setLeft(Node(val))
            else:
                self.getLeft().insert(val)
        elif val>=self.getData():
            if self.getRight()==None:
                self.setRight(Node(val))
            else:
                self.getRight().insert(val)

    def printInOrder(self):
        if self.getLeft()!=None:
            self.getLeft().printInOrder()
        print(self.getData())
        if self.getRight()!=None:
            self.getRight().printInOrder()
        return

n=Node(5)
n.insert(3)
n.insert(8)
n.insert(2)
n.insert(1)
n.insert(0)
n.printInOrder()


'''
for homework:
use preorder function as a template-define both inorder and postorder fuctions, for the following build_tree function
'''
