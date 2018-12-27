from Deque import Deque

def palChecker(aStr):
	charDeque=Deque()
	for ch in aStr:
		charDeque.addRear(ch)
	stillEqual=True
	while charDeque.size()>1 and stillEqual:
		first = charDeque.removeFront()
		last=charDeque.removeRear()
		if first!=last:
			stillEqual=False
	return stillEqual
	

usrIn=input("Please give a string for palindrome checking: ")
if palChecker(usrIn):
	nope=""
else: nope="not "
print("\""+usrIn+"\""+" is "+nope+"a palindrome")

