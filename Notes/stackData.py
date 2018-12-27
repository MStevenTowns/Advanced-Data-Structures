'''
USE 3.4
homework 1a is stack with append and prepend implementations
'''
class stackData:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
        #begging of list
        #self.items.insert(0,item)
    def pop(self):
        hold=self.items[-1]
        self.items=self.items[:-1]
        #hold=self.items[0]
        #self.items=self.items[1:]
        return hold
    def peek(self):
        return self.items[-1]
        #return self.items[0]
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items==[]
    def __str__(self):
        return str(self.items)
'''
stack=stackData()
print(stack.size())
print(stack.isEmpty())
stack.push(5)
print(stack.size())
print(stack.isEmpty())
print(stack)
stack.push(6)
stack.push(7)
stack.push(8)
stack.push(9)
stack.pop()
print(stack)
print(stack.peek())
print(stack.peek())

class Fraction:
    def __init__(self,top,bot):
        self.num=top
        self.den=bot
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    def __add__(self,f2):
        return Fraction(self.num*f2.den+f2.num*self.den,self.den*f2.den)
    def __sub__(self,f2):
        return Fraction(self.num*f2.den-f2.num*self.den,self.den*f2.den) 
    def __mul__(self,f2):
        return Fraction(self.num*f2.num,self.den*f2.den)
    def __div__(self,f2):
        return Fraction(self.num*f2.den,self.den*f2.num)
    def __truediv__(self,f2):
        return Fraction(self.num*f2.den,self.den*f2.num)

myFraction=Fraction(1,2)
print(myFraction)
newFraction=Fraction(1,2)
print(newFraction)
print("")
print(myFraction/newFraction)
print(myFraction+newFraction)
print(myFraction-newFraction)
print(myFraction*newFraction)
'''
