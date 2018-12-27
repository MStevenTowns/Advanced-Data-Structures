class Stack:
	#stack values are held in a list
    def __init__(self):
        self.items=[]
        
    #add a value to the top of the stack, using the last element in the list as the top of the stack
    def push(self,item):
		#append is used to reduce the number of move operations durring pop
        self.items.append(item)
    
    #save value from the top of the stack, remove that item from the stack and return that item
    def pop(self):
		#items[-1] is the last value in the list 'items'
        hold=self.items[-1]
        #make items equal to items from 0 through the second-to-last item, leaving the last item out
        self.items=self.items[:-1]
        return hold
    
    #return the top item on the stack, but do not pop it
    def peek(self):
        return self.items[-1]
    
    #return the size (an int) of the current stack
    def size(self):
        return len(self.items)
    
    #test if the stack contains any items and return True or False
    def isEmpty(self):
        return self.items==[]
    
    #convert the stack into a string using the built-in string representation of the list in python
    def __str__(self):
        return str(self.items)


