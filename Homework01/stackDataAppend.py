'''
M. Steven Towns 
9/25/16
Homework 1
Part A-1

THIS MUST BE RUN WITH PYTHON 3
'''

class stackDataAppend:
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

#input 
myStack=stackDataAppend()
while True:
    try:
        usrIn=int(input("\n\n1: Push\n2: Pop\n3: Peek\n4: Size\n5: Is It Empty?\n6: Print Stack\n7: Exit\nWhat would you like to do?: ").strip())
    except:
        usrIn=-1
    if(usrIn==1):
        print('Pushed: '+myStack.push(input("What would you like to push?: ")))
    elif(usrIn==2):
        print('Popped: '+myStack.pop())
    elif(usrIn==3):
        print('Peeked: '+myStack.peek())
    elif(usrIn==4):
        print('Size: '+myStack.size())
    elif(usrIn==5 ):
        print(myStack.isEmpty())
    elif(usrIn==6):
        print(myStack)
    elif(usrIn==7):
        exit()
    else: 
        print("Invalid input")
    
#end of input
