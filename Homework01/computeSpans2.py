'''
M. Steven Towns 
9/25/16
Homework 1
Part B-2

THIS MUST BE RUN WITH PYTHON 3

the stackData class is included in order to prevent it from running the 
main function in it's own file
'''

class stackData:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
       
        return item
    def pop(self):
        if self.isEmpty(): 
            return "No items in stack"
        hold=self.items[-1]
        self.items=self.items[:-1]
        
        return hold
    def peek(self):
        if self.isEmpty():
            return "No items in stack"
        return self.items[-1]
        
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items==[]
    def __str__(self):
        return str(self.items)

def computeSpans2(P):
    D=stackData()
    S=[]
    for i in range(len(P)):
        h=0
        done=False
        while not(D.isEmpty() or done):
            if P[i]>=P[D.peek()]:
                D.pop()
            else: 
                done=True
                #break

        if D.isEmpty():
            h=-1
        else:
            h=D.peek()
        S.append(i-h)
        D.push(i)
    return S
    
    
##input and formating, ignore for speed testing    
usrIn=input("Please give a list of stock prices separated by a space: ")
P=usrIn.strip().split(" ")
P=[float(i) for i in P]
##end of input and formating

print(computeSpans2(P))
